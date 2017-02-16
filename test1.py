# coding:utf-8
import os, statvfs
def getLinuxDiskInfo(path):
    if os.path.exists(path):
        vfs = os.statvfs(path)
        avail=round(vfs[statvfs.F_BAVAIL]*vfs[statvfs.F_BSIZE]/1024.0/1024/1024)
        size=round(vfs[statvfs.F_BLOCKS]*vfs[statvfs.F_BSIZE]/1024.0/1024/1024)
        used=size-avail
        use=round(used/size*100)
        Avail=str(avail)+'G'
        Size=str(size)+'G'
        Used=str(used)+'G'
        Use=str(use)+'%'
        ip=['192.168.3.175']
        for Ip in ip:
            return Ip,Size,Used,Avail,Use
tablehead = ['Ip','Size', 'Used', 'Avail', 'Use%', 'Mounted on']
directory = '/'
tablerows = getLinuxDiskInfo('/')
lenmax = []
for x in tablehead:
    print ("%-*s"%(15,x)),
print
for y in tablerows:
    print ("%-*s"%(15,y)),
print ("%-*s"%(15,directory))
