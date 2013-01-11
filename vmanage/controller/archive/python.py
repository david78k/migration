#!/usr/bin/python
import sys
import os
import time
import subprocess

origin = time.time()

cmd = "rocks run host gra1 \"dstat -n 1 1 | tail -1\" collate=y | awk '{print $2}'"
#bandwidth = os.system(cmd)
#print bandwidth

#from subprocess import call
#return_code = call (["ls", "-l"])

#print return_code

#proc = subprocess.Popen(['dstat', '-n', '1', '1'], stdout=subprocess.PIPE)
#output = proc.stdout.read()
#print output

#bandwidth = os.popen(cmd).read()
#print bandwidth

cmd = "free -m | grep Mem | awk '{print $2}'"
freemem = os.popen(cmd).read()
print 4 + 5, 10 / 3, freemem, int(freemem) * 100, eval(freemem) / 100

pms = []
for i in xrange(1, 9):
	vms = [x for x in range (1, 9)]
	pms.append(vms)
#	print i, pms[i - 1]

del pms[0][0]
del pms[7][7]
for i in xrange(1, 9):
	pass
#	print i, pms[i - 1]

#print pms

vms = [x for x in range (1, 9)]
#print vms
#for i in vms:
#	print i, vms[i - 1]

start = time.time()
time.sleep(1)
end = time.time()
elapsed = end - start
total_elapsed = end - origin
print "finish", elapsed, total_elapsed
