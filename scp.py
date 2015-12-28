#!/usr/bin/python
# -*- coding:utf-8 -*-
import os, datetime,time
host = '192.168.3.168'
print '%s   : 备份服务器IP是： %s\n' % (datetime.datetime.now(), host)
user = 'root'
# 备份的路径
bakup_file_path = '/data/backup/186/'+time.strftime('%Y%m')
print '%s   : 备份服务器的目录是： %s\n'% (datetime.datetime.now(), bakup_file_path)
base_dir = '/data/backup/'+time.strftime('%Y%m%d')+'/'
print '%s   : 即将备份的本地目录是： %s\n' % (datetime.datetime.now(), base_dir)
#备份文件名和文件路径
l = os.listdir(base_dir)
#查找最新的备份文件
l.sort(key=lambda fn: os.path.getmtime(base_dir + fn) if not os.path.isdir(base_dir + fn) else 0)
d = datetime.datetime.fromtimestamp(os.path.getmtime(base_dir + l[-1]))
file_name = l[-1]
file_path_and_name = base_dir + file_name
print '%s   : 本地目录中最新的备份文件是： %s\n'% (datetime.datetime.now(), l[-1])
print '%s   : 该文件的最后一次修改时间是： %s\n'% (datetime.datetime.now(),d)
# 统计导出的备份文件大小
file_size = os.path.getsize(file_path_and_name)
def format_file(format_file_size):
    size1=format_file_size/(1024.0*1024.0*1024.0)#GB
    size2=format_file_size/(1024.0*1024.0)#MB
    size3=format_file_size/1024.0#KB
    size4=format_file_size#B
    if      size1>1:
        print "%s   : 当前备份的文件大小是： %sGB\n"%(datetime.datetime.now(),round(size1,1))
    elif    size2>1:
        print "%s   : 当前备份的文件大小是： %sMB\n"%(datetime.datetime.now(),round(size2,1))
    elif    size3>1:
        print "%s   : 当前备份的文件大小是： %sKB\n"%(datetime.datetime.now(),round(size3,1))
    else:#这里对文件大小进行判断，当文件大于1M显示的是多少MB，如果当文件小于1M显示的是多少KB，利用round函数进行四舍五入
        print "%s   : 当前备份的文件大小是： %sB\n"%(datetime.datetime.now(),round(size4,3))
format_file(file_size)
#使用SCP导出到备份服务器
scp_parameter = user + '@' + host + ':'
scp_shell = 'scp ' + base_dir + file_name + ' ' + scp_parameter + bakup_file_path
print '%s   : scp的完整命令是： %s\n' % (datetime.datetime.now(), scp_shell)
print '---------------------------------------------------------------------\n'
print '%s   : ........正在传输到备份服务器..........\n'%datetime.datetime.now()
print
os.system(scp_shell)
print
print '%s   : ........传输到备份服务器结束..........\n'%datetime.datetime.now()
print '---------------------------------------------------------------------\n'
