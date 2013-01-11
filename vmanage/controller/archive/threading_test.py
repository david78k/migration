import time
import os
import platform
import socket
from threading import Thread

def sleeper(i):
    print "thread %d sleeps for 5 seconds" % i
    time.sleep(5)
    print "thread %d woke up" % i

def migrate(i):
	hostname = gethostname()
	#print hostname
	src = "gra1"
	dest = "grb1"
	vm = "gra1-" + str(i)
	if (hostname == "gr121"):
	#if (hostname is "gr121"):
		src = "grb1"
		dest = "gra1"

	cmd = "ssh " + src + " \"virsh migrate --live " + vm + " qemu+ssh://" + dest + "/system\""
	#cmd = "ssh gra1 \"virsh migrate --live gra1-1 qemu+ssh://grb1/system\""
	print cmd
	#os.popen(cmd)

def gethostname():
	hostname = socket.gethostname()
	cmd = "hostname -s"
	hostname = os.popen(cmd).read()
	return hostname.strip();

for i in range(3):
    #t = Thread(target=sleeper, args=(i,))
	t = Thread(target=migrate, args=(i + 1,))
	t.start()

#t1 = Thread(target=migrate, args=(2,))
#t2 = Thread(target=migrate, args=(3,))
#t2 = Thread(target=migrate, args=(3,))
#t1.start()
#t2.start()

#print os.uname()
#print platform.node()
#print socket.gethostname()
#print os.getenv('HOSTNAME')
print gethostname()

