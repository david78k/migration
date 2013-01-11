#!/usr/bin/python
import sys, os, subprocess
import time, socket
import threading
from threading import Thread
from collections import deque

pwnd = int(sys.argv[1])
vwnd = int(sys.argv[2])
sampletime = 5
sleep_interval = 0.1
NUM_PMs = 8
rvms = 64
origin = time.time()
pms = deque()

print str(pwnd) + "cpms-" +str(vwnd) + "cvms"

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
#	print i, pms[i - 1]
print

def getCVMs(i):
	cvms = 0
	cmd = "ps -ef | grep migrate | grep live | grep gra" + str(i) + " | wc -l"
	#cmd = "ps -ef | grep migrate | grep live | wc -l"
	cvms = os.popen(cmd).read()
	if not cvms:
		return 0
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
        os.popen(cmd)
	end = time.time()
	elapsed = end - start
	total_elapsed = end - origin
	print "finish", elapsed, total_elapsed

def getRVMs():
	cmd = "rocks run host \"virsh list\" | grep running | wc -l"
	rvms = os.popen(cmd).read()
	return int(rvms)

def migrateMultiple(cpms, cvms):
	# concurrent PMs
	pmfrom=1
	pmto=8

	vmfrom=1
	vmto=8

	origin = time.time()
#	print "finish 0 0"
	#print "finish " + str(origin) + " 0"

	basedir="/nfs/vmanage"

	for pm in range(pmfrom, pmto + 1, cpms):
        	pmend = pm + cpms 

		for vm in range(vmfrom, vmto + 1, cvms):
                        vmend = vm + cvms 

			for i in range(pm, pmend):
                                #sys.stdout.write ("pm" + str(i))
                                print "pm" + str(i), 
				list = []

				for j in range(vm, vmend):
					print "vm" + str(j),
		#			migrate(i, j)
	       				mt = Thread(target=migrate, args=(i , j))
			     		mt.start()
					list.append(mt)
                #                        $basedir/migrate $i $j $begin &
				print
                        #wait
			for thread in list:
				thread.join()
			#for thread in threading.enumerate():
				#thread.join()
			print

migrateMultiple(pwnd, vwnd)

# doesn't work
def migrate_multiple():
	pmstart = 0
	origin = time.time()
	rvms = getRVMs()
	i = 0
	while ( rvms > 0 ):
		cvms = getCVMs(i + 1)
		while (cvms >= vwnd):
			time.sleep(sleep_interval)
			cvms = getCVMs(i + 1)
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
		print "migrate", str(pwnd), str(vwnd), i, vm, rvms, pmstart
	
		i += 1	
		if (i == pwnd):
			i = pmstart
		if (i == 8):
			i = pmstart
		rvms -= 1
#		print "migrate", pwnd, vwnd, i, vm, rvms, pmstart
		#time.sleep(1)

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

#migrate_multiple()

#mt = Thread(target=migrate_multiple, args=())
#mt.start()

