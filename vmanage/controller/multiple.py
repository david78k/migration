#!/usr/bin/python

import sys
import os
import subprocess
import time, math
import socket
import threading
import random
import getopt
from threading import Thread
from collections import deque

# total number of physical machines (pms)
npms = 8
# vm window
vwnd = 1
# decrement factor
alpha = 0.75
threshold = 8
sampletime = 10

src_prefix = "gra"
dest_prefix = "grb"

sleep_interval = 0.1

cmd = "rocks run host gra1 \"dstat -n 1 1 | tail -1\" collate=y | awk '{print $2}'"

rvms = 6
# current VMs in transit
cvms = 0
origin = time.time()

cond = threading.Condition()
done = False

mq = deque() # migration queue
susq = deque() # suspended queue

golden_ratio = (3 - math.sqrt(5))/2

is_gridftp = False
parnum = 1

"""VM information class"""
class VMInfo:
	def __init__(self, id, pmid, pm, vm, memory):
		self.id = str(id)
		self.pmid = pmid
		self.pm = pm
		self.vm = vm
		self.memory = int(memory)

	def __repr__(self):
		return repr((self.id, self.pmid, self.pm, self.vm, self.memory))

	#def f(self):
	#	return 'hello world'

def gethostname():
        hostname = socket.gethostname()
        cmd = "hostname -s"
        hostname = os.popen(cmd).read()
        return hostname.strip();

# get VMs to migrate
def getVMs():
	vms = []
	k = 0
	for i in xrange(1, npms + 1):
		pmname = src_prefix + str(i)
		#pmname = "gra" + str(i)
		j = 1
		cmd = "ssh " + pmname + " \"virsh list | grep running\" | awk '{print $2}'"
		pvms = os.popen(cmd).read().strip()
		vmlist = pvms.split("\n")
		for vmname in vmlist:
			vmname = vmname.strip()
		
			cmd = "ssh " + pmname + " \"virsh dommemstat " + vmname + " | grep actual\" | awk '{print $2}'"
			if vmname:
				mem = os.popen(cmd).read().strip()
				k += 1
				vminfo = VMInfo(k, i, pmname, vmname, int(mem))
				#vminfo = (k, i, pmname, vmname, int(mem))
				vms.append(vminfo)
	return vms

# get the number of concurrent VMs in transit
def getCVMs():
	cvms = 0
	cmd = "ps -ef | grep migrate | grep live | wc -l"
	cvms = os.popen(cmd).read()
	cvms = int(cvms) - 1
	#print "cvms =", cvms
	return cvms		

# migrate using gridftp
# save vm on local disk and restore from remote
#def gridftp(vminfo):
def gridftp(src, dest, vm):
	global parnum
	#src = "grb1"
        #dest = "gra1"
        #vm = "gra1-1"
        dir = "/root/vmstate"
        vstat = dir + "/" + vm + ".vstat"
        # number of parallel connections
        #parnum=1

        cmd = "ssh " + src + " \"mkdir -p " + dir + "; ssh " + dest + " mkdir -p " + dir + "\""
	print cmd
	os.popen(cmd)

        cmd = "ssh " + src + " \"rm -rf " + vstat + "; ssh " + dest + " rm -rf " + vstat + "\""
	print cmd
	os.popen(cmd)

        print "saving " + vm + " to " + vstat + " ... "
        begin = time.time()
        cmd = "ssh " + src + " virsh save " + vm + " " + vstat
	print cmd
	os.popen(cmd)
        end = time.time()
        saving_time = end - begin

        print "transferring " + vstat + " to " + dest + " ... "
        begin = time.time()
        cmd = "ssh " + src + " globus-url-copy -p " + str(parnum) + " " + vstat + " sshftp://" + dest +"/" + vstat
	print cmd
	os.popen(cmd)
        end = time.time()
        transfer_time = end - begin

        print "restoring " + vstat + " from " + dest + "... "
        begin = time.time()
        cmd = "ssh " + src + " ssh " + dest + " virsh restore " + vstat
	print cmd
	os.popen(cmd)
        end = time.time()
        restore_time = end - begin

	total_time = saving_time + transfer_time + restore_time
	print "gridftp",total_time,saving_time,transfer_time,restore_time

# migrate a vm with a vminfo
def migrate(vminfo):
	global cvms, cond, mq

	pmid = vminfo.pmid
	vm = vminfo.vm

	src = src_prefix + str(pmid)
	dest = dest_prefix + str(pmid)

        cmd = "ssh " + src + " \"virsh migrate --live " + str(vm) + " qemu+ssh://" + dest + "/system\""
        print cmd

	start = time.time()
	if is_gridftp:
		gridftp(src, dest, vm)
	else:
		os.popen(cmd)

	#time.sleep(5)
	end = time.time()
	elapsed = end - start
	total_elapsed = end - origin

	cond.acquire()
	#print 'cvms',cvms
	cvms = cvms - 1
	#printVMInfoIDs(mq)
	#print mq, vminfo

	try:
		mq.remove(vminfo)
	except ValueError:
		print "Could not remove vminfo from mq."
	except:
		print "Unexpected error:", sys.exc_info()[0]
	print "finish", elapsed, total_elapsed

	cond.notify()
	cond.release()

# migrate multiple vms
def migrate_multiple(list):
	global cvms, vwnd, cond, done, mq, susq, vminfolist

	vminfolist = list
	i = 0
	#for vminfo in list:
	while list or susq:
		i += 1
		#print vminfo

		# check if suspended queue is empty
		if susq:
			vminfo = susq.pop()
			resume (vminfo)
			mq.append(vminfo)
		elif list:
			vminfo = list.pop(0)
		        t = Thread(target=migrate, args=(vminfo,))
		        t.start()
			print vminfo.id + " has started."
			mq.append(vminfo)
		else:
			continue
		#print mq
		printQueues()
		#printVMInfoIDs(mq)

		cvms = cvms + 1
		time.sleep(sleep_interval)
		cond.acquire()
		while True:
			rvwnd = round(vwnd)
			if (cvms < rvwnd):
				break
			elif (cvms > rvwnd ):
				rest = int(cvms) - int(rvwnd)
				print "cvms=" + str(cvms) + " rvwnd=" + str(rvwnd) + " rest=" + str(rest) + " len(mq)=" + str(len(mq))
				rest = min(rest, len(mq))
				for j in range(int(rest)):
					vminfo = mq.popleft()
					suspend(vminfo)
					cvms = cvms - 1
	#				susq.append(vminfo)	
			print "waiting ..."
			cond.wait()
		cond.release()
		print "released."
	done = True
	print "migrator done."

def getBandwidth():
        total = 0
        cmd = "rocks run host \"dstat -n -N eth1 " + str(sampletime) + " 1 | tail -1\" | awk '{print $2}' | sed 's/B//g;s/M/000000/g;s/k/000/g'"

        p = os.popen(cmd,"r")
        while 1:
                line = p.readline().strip()
                if not line: break
#               print line.strip()
                total += int(line)
        return total

# suspend specific vm on pm with vminfo
def suspend(vminfo):
	pm = vminfo.pm
	vm = vminfo.vm
	cmd = "ssh " + pm + " virsh migrate-setspeed " + vm + " 0"	
	#mq.remove(vminfo)
	susq.append(vminfo)		
	print vminfo.id + " has been suspended."
	printQueues()

def resume(vminfo):
	pm = vminfo.pm
	vm = vminfo.vm
	maxbandwidth = 120 # MB
	cmd = "ssh " + pm + " virsh migrate-setspeed " + vm + " " + str(maxbandwidth)
	#susq.remove(vminfo)
	#mq.append(vminfo)
	print vminfo.id + " has been resumed."

def control():
	global vwnd, threshold, done
	vwnd = 1
	# total bandwidth of the previous iteration
	totalprev = 0
	# average bandwidth of the previous iteration
	avgprev = 0
	congested = False
	phase = "ss" # slow start 

	print "phase vwnd total avg totalvms threshold"
	while not done:
	        total = getBandwidth()
		#totalvms = getCVMs()
		totalvms = vwnd
       	 	avg = total / totalvms

	        print "controller", phase, vwnd, total, avg, totalvms, threshold

		cond.acquire()
		if (phase == "ss"):
			# if congestion occurs
			if ( avg < avgprev):
				vwnd = vwnd * alpha
				threshold = vwnd
				phase = "ca"	
			else:
				if ( vwnd >= threshold):
					phase = "ca"
					
					vwnd += 1
				else:
                			vwnd *= 2
       		else:
                	if ( avg < avgprev ):
				vwnd = vwnd * alpha
				threshold = vwnd
				#suspend(vm)
                	else:
                        	vwnd += 1

        	if ( vwnd < 1 ):
                	vwnd = 1
		#vwnd = int(vwnd)

		cond.notify()
		cond.release()

        	totalprev = total
        	avgprev = avg

#golden section search
def G(N):
	global vwnd
        #time.sleep(1)
	cond.acquire()
	vwnd = N
	cond.notify()
	cond.release()

	bw = getBandwidth()
        return bw
        #return bw/N
        #return -2*((N - 6)**2) + 72
	
def search_bracket():
        #global alpha
        iter = 1
        N = 1; N_1 = 1; N_2 = 1

        G_N = 0; G_N_1 = 0; G_N_2 = 0
        print "iter, N, G_N, G_N_1, G_N_2, (G_N >= G_N_1)"

        while True:
                G_N = G(N)
                #G_N = getBandwidth()
                print iter, N, G_N, G_N/N, G_N_1, G_N_2, (G_N >= G_N_1)
                #if G_N < G_N_1 and iter > 10:
                if G_N < G_N_1:
                        break

                G_N_1 = G_N
                N_2 = N_1
                N_1 = N
                N *= 2
                iter += 1
                #time.sleep(1)
        return (N_2, N_1, N, G_N_1)

def golden_section_control():
	bracket = search_bracket()
	print bracket
	#print "vwnd total avg"
        #print "iter, N, G_N, G_N_1, G_N_2, (G_N >= G_N_1)"
	golden_section_search(bracket)

def golden_section_search((l, m, r, G_m)):
	global done, golden_ratio

	if not done:
	#while not done:
                N = m + (r - m)*golden_ratio
                if (r - m) < (m - l):
                        N = l + (m - l)*golden_ratio
                N = round(N)
		
                G_N = G(N)
                #G_m = G(m)
                print N, G_N, G_N/N, G_m
                if G_N > G_m:
                        if N > m:
                                golden_section_search((m, N, r, G_N))
                        else:
                                golden_section_search((l, N, m, G_N))
                else:
                        if N > m:
                                golden_section_search((l, m, N, G_m))
                        else:
                                golden_section_search((N, m, r, G_m))

def printList(list):
	for item in list:
		print item

def printQueues():
	global mq, susq, vminfolist

	print "list=[",
	for item in vminfolist:
		print item.id,
	print "]",

	print "mq=[",
	for item in mq:
		print item.id,
	print "]", 

	print "susq=[",
	for item in susq:
		print item.id,
	print "]"


def printVMInfoIDs(list):
	print "[",
	for item in list:
		print item.id,
	print "]"


def main(argv):
	sched = "lf"

	global vwnd, parnum, is_gridftp

	inputfile = ''
	outputfile = ''

	filename = os.path.basename(__file__)
	usage = filename + ' -s <schedule> -v <vm window> -g <number of gridftp parallel connections>' 

	try:
		opts, args = getopt.getopt(argv,"hs:v:d:g:",["sched=","vwnd=","delay=","gridftp="])
	except getopt.GetoptError:
		print usage
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print usage
			sys.exit()
		elif opt in ("-s", "--sched"):
			sched = arg
		elif opt in ("-v", "--vwnd"):
			vwnd = int(arg)
		elif opt in ("-g", "--gridftp"):
			parnum = int(arg)
			is_gridftp = True
		elif opt in ("-d", "--delay"):
			delay = arg
	print 'scheduling is', sched
	print 'vm window is', vwnd

	hostname = gethostname()

	if (hostname == "gr121"):
		global src_prefix, dest_prefix
		tmp = src_prefix
		src_prefix = dest_prefix
		dest_prefix = tmp

	origin = time.time()

	# migrate heterogeneous VMs
	vms = getVMs()
	list =[]

	if (sched == "sf"):
		list = sorted(vms, key=lambda vminfo: vminfo.memory)   # sort by memory size
	elif (sched == "lf"):
		list = sorted(vms, key=lambda vminfo: vminfo.memory, reverse=True)   # sort by memory size
	elif (sched == "rand"):
		list = sorted(vms)
		random.shuffle(list)
	else: 
		list = vms
	
	i = 0
	for item in list:
		i += 1
		item.id = str(i)

	printList(list)

	#mt = Thread(target=migrate_multiple, args=(list))
	#mt.start()
# migrate VMs with the controller for homogeneous memeory size
	if (vwnd == 0):
		ct = Thread(target=control, args=())
		#ct = Thread(target=golden_section_control, args=())
		ct.start()
	#	control()

	migrate_multiple(list)

if __name__ == "__main__":
   main(sys.argv[1:])

