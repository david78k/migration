#!/usr/bin/python
import sys, os, subprocess
import time, socket
from threading import Thread
from collections import deque

vwnd = 1
pwnd = 1
sampletime = 5
sleep_interval = 0.1
#offset = 0
NUM_PMs = 8
rvms = 64
origin = time.time()
pms = deque()

def gethostname():
        hostname = socket.gethostname()
        cmd = "hostname -s"
        hostname = os.popen(cmd).read()
        return hostname.strip();

hostname = gethostname()

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
	#print "cvms =", cvms
	return cvms		

# migrate pm-vm
def migrate(i, j):
#        hostname = gethostname()
	src = "gra" + str(i)
	dest = "grb" + str(i)
        vm = "gra" + str(i) + "-" + str(j)
        if (hostname == "gr121"):
                src = "grb" + str(i)
                dest = "gra" + str(i)

        cmd = "ssh " + src + " \"virsh migrate --live " + vm + " qemu+ssh://" + dest + "/system\""
        #print cmd
	start = time.time()
        #os.popen(cmd)
	end = time.time()
	elapsed = end - start
	total_elapsed = end - origin
	print "finish", elapsed, total_elapsed

def getRVMs():
	cmd = "rocks run host \"virsh list\" | grep running | wc -l"
	rvms = os.popen(cmd).read()
	return int(rvms)

def migrate_multiple():
	pmstart = 0
	origin = time.time()
	rvms = getRVMs()
	i = 0
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
		#"pwnd=", pwnd, ", vwnd=", vwnd, ", pm=", i, ", vm=", vm, ", rvms=", rvms, ", pmstart=", pmstart
		print "migrate", pwnd, vwnd, i, vm, rvms, pmstart
	
		i += 1	
		if (i == pwnd):
			i = pmstart
		if (i == 8):
			i = pmstart
		rvms -= 1
		#time.sleep(1)

#	print
#	print pms	

#	print getCVMs()
#	print getRVMs()

#migrate_multiple()

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
#		print line.strip()
		total += int(line)
	return total	

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
			congested = False
	else:	
	        if ( avg < avgprev ):
	                vwnd -= 1 
	                #vwnd=$(( vwnd * alpha ))
			congested = True
	        else:
	                vwnd += 1 
	                pwnd += 1 

	        #if ( total < totalprev ):
	        #        pwnd -= 1 
	        #else:
	        #        pwnd += 1

        if ( vwnd < 1 ):
                vwnd = 1

        if ( pwnd < 1 ):
                pwnd = 1

	if ( pwnd > NUM_PMs ):
		pwnd = NUM_PMs

        totalprev = total
        avgprev = avg


