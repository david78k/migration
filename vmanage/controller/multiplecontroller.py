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
rvms = 64
# current VMs in transit
cvms = 0
origin = time.time()

cond = threading.Condition()
done = False

def gethostname():
        hostname = socket.gethostname()
        cmd = "hostname -s"
        hostname = os.popen(cmd).read()
        return hostname.strip();

# get VMs to migrate
def getVMs():
	vms = []
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
				vms.append((i, pmname, vmname, int(mem)))
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
def migrate(i, j):
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

# migrate a vm with a pm id
def migrate_hetero(pmid, vm):
	global cvms, cond
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
	print "finish", elapsed, total_elapsed

	cond.notify()
	cond.release()

# migrate multiple vms
def migrate_multiple(list):
	global cvms, vwnd, cond, done
	i = 0
	for vminfo in list:
		i += 1
		#print vminfo
		pmid = vminfo[0]
		pm = vminfo[1]
		vm = vminfo[2]
		mem = vminfo[3]
	#	print '[',i, pm, vm, mem,']'

		if (susQ is empty):
		        t = Thread(target=migrate_hetero, args=(pmid, vm))
		        t.start()
		else:
			vminfo = susQ.remove()
			resume (vminfo)
		cvms = cvms + 1
		time.sleep(sleep_interval)
		cond.acquire()
		while True:
			if (cvms < vwnd):
				break
			else if (cvms > vwnd ):
				vminfo = mQ.remove()
				suspend(vminfo)
			
				susQ.add(vminfo)	
			cond.wait()
		cond.release()
	done = True

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

# suspend vms in a vminfo list
def suspend(vminfolist):
	for vminfo in vminfolist:
		pm = vminfo[1]
		vm = vminfo[2]
		suspend(pm, vm)	

# suspend specific vm on pm
def suspend(pm, vm):
	cmd = "ssh " + pm + " virsh migrate-setspeed " + vm + " 0"	

def resume(pm, vm):
	maxbandwidth = 120 # MB
	cmd = "ssh " + pm + " virsh migrate-setspeed " + vm + " " + maxbandwidth	

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

