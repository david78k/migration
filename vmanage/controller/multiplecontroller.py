#!/usr/bin/python

import sys
import os
import subprocess
import time
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
# pm window
pwnd = 8
# decrement factor
alpha = 0.75
threshold = 8
sampletime = 5

src_prefix = "gra"
dest_prefix = "grb"

sleep_interval = 0.1

cmd = "rocks run host gra1 \"dstat -n 1 1 | tail -1\" collate=y | awk '{print $2}'"

pmstart = 0
offset = 0
rvms = 6
# current VMs in transit
cvms = 0
origin = time.time()

cond = threading.Condition()
done = False

mq = deque() # migration queue
susq = deque() # suspended queue

"""VM information class"""
class VMINFO:
	#def __init__(self, realpart, imagpart):
		#self.r = realpart
		#self.i = imagpart
	def __init__(self, pmid, pm, vm, memory):
		self.pmid = pmid
		self.pm = pm
		self.vm = vm
		self.mem = memory

	i = 12345
	def f(self):
		return 'hello world'

def gethostname():
        hostname = socket.gethostname()
        cmd = "hostname -s"
        hostname = os.popen(cmd).read()
        return hostname.strip();

# get VMs to migrate
def getVMs():
	vms = []
	k = 0
	#npms = 8
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
				vminfo = (i, pmname, vmname, int(mem))
				#vminfo = (k, i, pmname, vmname, int(mem))
				vms.append(vminfo)
				#vms.append((i, pmname, vmname, int(mem)))
				print k,vminfo
	return vms

# get the number of concurrent VMs in transit
def getCVMs():
	cvms = 0
	cmd = "ps -ef | grep migrate | grep live | wc -l"
	cvms = os.popen(cmd).read()
	cvms = int(cvms) - 1
	#print "cvms =", cvms
	return cvms		

# migrate pm-vm
def migrate_old(i, j):
	src = "gra" + str(i)
	dest = "grb" + str(i)
        vm = "gra" + str(i) + "-" + str(j)
        if (hostname == "gr121"):
                src = "grb" + str(i)
                dest = "gra" + str(i)

        cmd = "ssh " + src + " \"virsh migrate --live " + vm + " qemu+ssh://" + dest + "/system\""
        print cmd
	start = time.time()
        os.popen(cmd)
	end = time.time()
	elapsed = end - start
	total_elapsed = end - origin
	print "finish", elapsed, total_elapsed

# migrate a vm with a vminfo
#def migrate(vminfo):
def migrate(pmid, pm, vm, memory):
	global cvms, cond, mq
	#pmid = vminfo[0]
	#pm = vminfo[1]
	#vm = vminfo[2]
	vminfo = (pmid, pm, vm, int(memory))

	src = src_prefix + str(pmid)
	dest = dest_prefix + str(pmid)

        cmd = "ssh " + src + " \"virsh migrate --live " + str(vm) + " qemu+ssh://" + dest + "/system\""
        print cmd

	start = time.time()
	os.popen(cmd)
	#time.sleep(5)
	end = time.time()
	elapsed = end - start
	total_elapsed = end - origin

	cond.acquire()
	#print 'cvms',cvms
	cvms = cvms - 1
	print mq, vminfo
	try:
		mq.remove(vminfo)
	except ValueError:
		print "Could not remove vminfo from mq."
	except:
		print "Unexpected error:", sys.exc_info()[0]
	#except:
		#pass
	print "finish", elapsed, total_elapsed

	cond.notify()
	cond.release()

# migrate a vm with a pm id
def migrate_hetero(pmid, vm):
	global cvms, cond
	vminfo = [pmid, vm]
	src = src_prefix + str(pmid)
	dest = dest_prefix + str(pmid)
        cmd = "ssh " + src + " \"virsh migrate --live " + str(vm) + " qemu+ssh://" + dest + "/system\""
        print cmd

	start = time.time()
	os.popen(cmd)
	#time.sleep(5)
	end = time.time()
	elapsed = end - start
	total_elapsed = end - origin

	cond.acquire()
	#print 'cvms',cvms
	cvms = cvms - 1
	#mq.remove(vminfo)
	print "finish", elapsed, total_elapsed

	cond.notify()
	cond.release()

# migrate multiple vms
def migrate_multiple(list):
	global cvms, vwnd, cond, done, mq, susq

	i = 0
	for vminfo in list:
		i += 1
		#print vminfo
		pmid = vminfo[0]
		pm = vminfo[1]
		vm = vminfo[2]
		mem = vminfo[3]
	#	print '[',i, pm, vm, mem,']'

		# check if suspended queue is empty
		if not susq:
		        #t = Thread(target=migrate_hetero, args=(pmid, vm))
		        t = Thread(target=migrate, args=(vminfo))
		        t.start()
		else:
			vminfo = susq.pop()
			resume (vminfo)
		mq.append(vminfo)
		print mq

		cvms = cvms + 1
		time.sleep(sleep_interval)
		cond.acquire()
		while True:
			if (cvms < vwnd):
				break
			elif (cvms > vwnd ):
				rest = int(cvms) - int(vwnd)
				print cvms, vwnd, rest, len(mq)
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
        #print cmd
        #os.system(cmd)
        #subprocess.call([cmd])

        p = os.popen(cmd,"r")
        while 1:
                line = p.readline().strip()
                if not line: break
#               print line.strip()
                total += int(line)
        return total

# suspend specific vm on pm with vminfo
def suspend(vminfo):
	pm = vminfo[1]
	vm = vminfo[2]
	cmd = "ssh " + pm + " virsh migrate-setspeed " + vm + " 0"	
	#mq.remove(vminfo)
	susq.append(vminfo)		
	print "suspended."

def resume(vminfo):
	pm = vminfo[1]
	vm = vminfo[2]
	maxbandwidth = 120 # MB
	cmd = "ssh " + pm + " virsh migrate-setspeed " + vm + " " + str(maxbandwidth)
	#susq.remove(vminfo)
	#mq.append(vminfo)
	print "resumed."

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
	        #print "controller", rvms, total, avg, vwnd, totalvms

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
		vwnd = int(vwnd)

		cond.notify()
		cond.release()

        	totalprev = total
        	avgprev = avg
	
def main(argv):
	sched = "lf"

	global vwnd

	inputfile = ''
	outputfile = ''

	filename = os.path.basename(__file__)
	usage = filename + ' -s <schedule> -v <vmwindow>' 

	try:
		opts, args = getopt.getopt(argv,"hs:v:d:",["sched=","vwnd=","delay="])
		#opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print usage
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print usage
			#print 'test.py -s <schedule> -v <vmwindow> -d <delay>'
			sys.exit()
		elif opt in ("-s", "--sched"):
			sched = arg
		elif opt in ("-v", "--vwnd"):
			vwnd = int(arg)
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
	i = 0

	# migrate heterogeneous VMs
	vms = getVMs()
	list =[]

	if (sched == "sf"):
		list = sorted(vms, key=lambda vm: vm[3])   # sort by memory size
	elif (sched == "lf"):
		list = sorted(vms, key=lambda vm: vm[3], reverse=True)   # sort by memory size
	elif (sched == "rand"):
		list = sorted(vms)
		random.shuffle(list)
	else: 
		list = vms
	
	#mt = Thread(target=migrate_multiple, args=(list))
	#mt.start()
# migrate VMs with the controller for homogeneous memeory size
	if (vwnd == 0):
		ct = Thread(target=control, args=())
		ct.start()
	#	control()

	migrate_multiple(list)

if __name__ == "__main__":
   main(sys.argv[1:])

