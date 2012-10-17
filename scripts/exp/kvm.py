import libvirt

conn=libvirt.open("qemu:///system")
names = conn.listDefinedDomains()
print names

nums = conn.numOfDomains()
print nums

name= "vm512-16"
dom = conn.lookupByName(name)
print dom.info()
#print dom.getJobInfo()
#print conn.getInfo()
#print conn.migrate()

names = conn.listDomainsID()
#print names
#for item in names:
#	dom=conn.lookupByID(item)
#	print dom.info()

clist = dir(conn)
for item in clist:
	print item
