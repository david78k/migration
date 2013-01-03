#!/usr/bin/python

import sys
import os
import subprocess
import time
import socket
from threading import Thread
from collections import deque

# total number of physical machines (pms)
npms = 8
# vm window
vwnd = 8
# pm window
pwnd = 8

src_prefix = "gra"
dest_prefix = "grb"

sleep_interval = 0.1

cmd = "rocks run host gra1 \"dstat -n 1 1 | tail -1\" collate=y | awk '{print $2}'"

pmstart = 0
offset = 0
rvms = 64
origin = time.time()

def gethostname():
        hostname = socket.gethostname()
        cmd = "hostname -s"
        hostname = os.popen(cmd).read()
        return hostname.strip();

hostname = gethostname()

pms = deque()
for i in xrange(1, 9):
	vms = [x for x in range (1, 9)]
	#vms = [x + i * 10 for x in range (1, 9)]
	pms.append(vms)
	#print i, pms[i - 1]
print

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

if (hostname == "gr121"):
	tmp = src_prefix
	src_prefix = dest_prefix
	dest_prefix = tmp

origin = time.time()
i = 0

# migrate heterogeneous VMs
vms = getVMs()
list = sorted(vms, key=lambda vm: vm[3])   # sort by memory size
	
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
        print cmd
        os.popen(cmd)

#while ( pms ):
'''
while ( rvms > 0 ):
	cvms = getCVMs()
	while (cvms >= vwnd):
		time.sleep(sleep_interval)
		cvms = getCVMs()
	vms = pms[i]
	while ( not vms ):
		i += 1
		if ( i == 8 ):
			i = pmstart
		vms = pms[i]
	
	vm = vms.pop(0)

        t = Thread(target=migrate, args=(i + 1, vm))
        t.start()
	
	if ( not vms and i == pmstart):
		pmstart += 1
	#	pms.pop(i)
	#print "i=", i, ", len(pms)=", len(pms), ", vms=", vms
	print "pwnd=", pwnd, ", vwnd=", vwnd, ", pm=", i, ", vm=", vm, ", rvms=", rvms, ", pmstart=", pmstart
	#print "pm =", i, ", vm =", vm, ", offset =", offset
	
	i += 1	
	if (i == pwnd):
		i = pmstart
	if (i == 8):
		i = pmstart
	rvms -= 1
	#offset += 1
	#if ( offset == pwnd ):
#		offset = 0

print
print pms	

print getCVMs()
'''

# migrate VMs with homogeneous memeory size
'''
#while ( pms ):
while ( rvms > 0 ):
	cvms = getCVMs()
	while (cvms >= vwnd):
		time.sleep(sleep_interval)
		cvms = getCVMs()
	vms = pms[i]
	while ( not vms ):
		i += 1
		if ( i == 8 ):
			i = pmstart
		vms = pms[i]
	
	vm = vms.pop(0)

        t = Thread(target=migrate, args=(i + 1, vm))
        t.start()
	
	if ( not vms and i == pmstart):
		pmstart += 1
	#	pms.pop(i)
	#print "i=", i, ", len(pms)=", len(pms), ", vms=", vms
	print "pwnd=", pwnd, ", vwnd=", vwnd, ", pm=", i, ", vm=", vm, ", rvms=", rvms, ", pmstart=", pmstart
	#print "pm =", i, ", vm =", vm, ", offset =", offset
	
	i += 1	
	if (i == pwnd):
		i = pmstart
	if (i == 8):
		i = pmstart
	rvms -= 1
	#offset += 1
	#if ( offset == pwnd ):
#		offset = 0

print
print pms	

print getCVMs()
'''
