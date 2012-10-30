import sys
import os
import subprocess
import time
import socket
from threading import Thread
from collections import deque

vwnd = 4
pwnd = 4

cmd = "rocks run host gra1 \"dstat -n 1 1 | tail -1\" collate=y | awk '{print $2}'"
#bandwidth = os.system(cmd)
#print bandwidth

pmstart = 0
offset = 0
rvms = 64

def gethostname():
        hostname = socket.gethostname()
        cmd = "hostname -s"
        hostname = os.popen(cmd).read()
        return hostname.strip();

hostname = gethostname()

#pms = []
pms = deque()
for i in xrange(1, 9):
	vms = [x for x in range (1, 9)]
	#vms = [x + i * 10 for x in range (1, 9)]
	pms.append(vms)
	print i, pms[i - 1]
print

def getCVMs():
	cvms = 0
	cmd = "ps -ef | grep migrate | grep live | wc -l"
	#cmd = "ps -ef | grep migrate | grep live"
	cvms = os.popen(cmd).read()
	cvms = int(cvms) - 1
	print "cvms =", cvms
	return cvms		

def migrate(i, j):
#        hostname = gethostname()
        #print hostname
	src = "gra" + str(i)
	dest = "grb" + str(i)
        vm = "gra" + str(i) + "-" + str(j)
        if (hostname == "gr121"):
        #if (hostname is "gr121"):
                src = "grb" + str(i)
                dest = "gra" + str(i)

        cmd = "ssh " + src + " \"virsh migrate --live " + vm + " qemu+ssh://" + dest + "/system\""
        #cmd = "ssh gra1 \"virsh migrate --live gra1-1 qemu+ssh://grb1/system\""
        print cmd
        #os.popen(cmd)

i = 0
#while ( pms ):
while ( rvms > 0 ):
	cvms = getCVMs()
	while (cvms >= vwnd):
		time.sleep(1)
		cvms = getCVMs()
	vms = pms[i]
	while ( not vms ):
		i += 1
		if ( i == 8 ):
			i = pmstart
		vms = pms[i]
	
	vm = vms.pop(0)

	src = "gra" + str(i + 1)
	dest = "grb" + str(i + 1)
	cmd = "ssh " + src + " \"virsh migrate --live " + src + "-" + str(vm) + " qemu+ssh://" + dest + "/system\""
	#print cmd
#	migrate(vm)
        t = Thread(target=migrate, args=(i + 1, vm))
        t.start()
#	os.popen(cmd)
	
	if ( not vms and i == pmstart):
		pmstart += 1
	#	pms.pop(i)
	#print "i=", i, ", len(pms)=", len(pms), ", vms=", vms
	print "pm =", i, ", vm =", vm, ", rvms =", rvms, ", pmstart =", pmstart
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

