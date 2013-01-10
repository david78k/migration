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

def migrate_hetero(pmid, vm):
	src = src_prefix + str(pmid)
	dest = dest_prefix + str(pmid)
        cmd = "ssh " + pm + " \"virsh migrate --live " + str(vm) + " qemu+ssh://" + dest + "/system\""
        print cmd
	os.popen(cmd)
	global cvms
	cond.acquire()
	cvms = cvms - 1
	cond.notify()
	cond.release()

def migrate_multiple():
	global cvms
	for vminfo in list:
		#print vminfo
		pmid = vminfo[0]
		pm = vminfo[1]
		vm = vminfo[2]
		mem = vminfo[3]
		print pmid, pm, vm, mem

		src = src_prefix + str(pmid)
		dest = dest_prefix + str(pmid)
	        cmd = "ssh " + pm + " \"virsh migrate --live " + str(vm) + " qemu+ssh://" + dest + "/system\""
#        print cmd
#        os.popen(cmd)

	        t = Thread(target=migrate_hetero, args=(pmid, vm))
#	        t.start()

		cvms = cvms + 1
		time.sleep(sleep_interval)
'''
		cond.acquire()
		while True:
			if (cvms < vwnd):
				break
			cond.wait()
		cond.release()
'''

def control():
	totalprev = 0
	avgprev = 0
	congested = False

	mt = Thread(target=migrate_multiple, args=())
	mt.start()

	print "rvms total avg pwnd vwnd totalvms"
	while True:
	        rvms = getRVMs()
	        if (rvms == 0):
	                break

	        total = getBandwidth()
        	totalvms = pwnd * vwnd
       	 	avg = total / totalvms

	        print "controller", rvms, total, avg, pwnd, vwnd, totalvms

		if congested:
                	if ( avg < avgprev ):
                	        pwnd -= 1
                        #vwnd=$(( vwnd * alpha ))
               		else:
                	        pwnd += 1
                	        vwnd += 1
                	        congested = False
       		else:
                	if ( avg < avgprev ):
                       		vwnd -= 1
                        #vwnd=$(( vwnd * alpha ))
                        	congested = True
                	else:
                        	vwnd += 1
                        	pwnd += 1
        	if ( vwnd < 1 ):
                	vwnd = 1

        	if ( pwnd < 1 ):
                	pwnd = 1

        	if ( pwnd > NUM_PMs ):
                	pwnd = NUM_PMs

        	totalprev = total
        	avgprev = avg
	
def main(argv):
	sched = "LF"
	sched = "SF"
#sched = "rand"

	global vwnd

	inputfile = ''
	outputfile = ''

	try:
		opts, args = getopt.getopt(argv,"hs:v:d:",["sfile=","vfile=","dfile="])
		#opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -s <schedule> -v <vmwindow> -d <delay>'
			sys.exit()
		elif opt in ("-s", "--sched"):
			sched = arg
		elif opt in ("-v", "--vwnd"):
			vwnd = arg
		elif opt in ("-d", "--delay"):
			delay = arg
	print 'schedule is', sched
	print 'vm window is', vwnd
	#print 'delay is', delay

	hostname = gethostname()

#	pms = deque()
#	for i in xrange(1, 9):
#		vms = [x for x in range (1, 9)]
#		pms.append(vms)
#	print

	if (hostname == "gr121"):
		tmp = src_prefix
		src_prefix = dest_prefix
		dest_prefix = tmp

	origin = time.time()
	i = 0

	# migrate heterogeneous VMs
'''
	vms = getVMs()

	if (sched == "SF"):
		list = sorted(vms, key=lambda vm: vm[3])   # sort by memory size
	elif (sched == "LF"):
		list = sorted(vms, key=lambda vm: vm[3], reverse=True)   # sort by memory size
	elif (sched == "rand"):
		list = sorted(vms)
		random.shuffle(list)
	else: 
		list = vms
'''
	
if __name__ == "__main__":
   main(sys.argv[1:])

# migrate VMs with the controller for homogeneous memeory size
#if (vwnd == 0):
#	control()

#migrate_multiple()

