# coding:utf-8
import os, statvfs
#因为statvfs只能在Linux下运行，该脚本只适用于Linux系统
#vfs的结果是：posix.statvfs_result(f_bsize=4096,
# f_frsize=4096, f_blocks=12868767,
# f_bfree=9749783, f_bavail=9094423,
#  f_files=3276800, f_ffree=3116352, f_favail=3116352, f_flag=4096, f_namemax=255)

def getLinuxDiskInfo(path):
    if os.path.exists(path):
        vfs = os.statvfs(path)
        #这个具体的原理弄不明白，先这样用着吧
        #VFS和stavfs
        #具体的是获取磁盘的大小，得到的结果是byte，然后除于3个1024，就得到了GB为单位
        #这4个结果分别是，总磁盘大小、使用了多少磁盘大小，可用磁盘大小，使用率，挂载的磁盘位置
        #------计算结果
        avail=round(vfs[statvfs.F_BAVAIL]*vfs[statvfs.F_BSIZE]/1024.0/1024/1024)
        size=round(vfs[statvfs.F_BLOCKS]*vfs[statvfs.F_BSIZE]/1024.0/1024/1024)
        used=size-avail
        use=round(used/size*100)
        #---------把输出格式改为带后缀的
        Avail=str(avail)+'G'
        Size=str(size)+'G'
        Used=str(used)+'G'
        Use=str(use)+'%'
        return Size,Used,Avail,Use


#定义表头
tablehead = ['Size', 'Used', 'Avail', 'Use%', 'Mounted on']
directory = '/'#定义要分析的目录
tablerows = getLinuxDiskInfo('/')#把结果写到表格里面
lenmax = []#先分析一下表头最长的字段，然后用这个字段当做下面格式化的显示长度
for x in tablehead:
    lenmax.append(len(x))
e = max(lenmax)
for x in tablehead:
        #使用下面的方式是：'%+a.bs'。意思是：%s代表字符串显示
        #+代表右对齐，-是左对齐
        #a是代表的显示长度width
        #.代表的是小数点后的位数pricision
        #b代表小数点后的具体位数
        #这里是字符串，不要小数点后面的就行。直接写("%+*s" %(e, x))
    print ("%-*s"%(e,x)),
print
for y in tablerows:
    print ("%-*s"%(e,y)),
print ("%-*s"%(e,directory))
