#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, datetime
import sys

reload(sys)
print '---------------------------------------------------------------------\n'
print '%s   : ........正在进行备份请稍后..........\n'%datetime.datetime.now()
print
print '%s   : 系统当前默认字符集是%s' % (datetime.datetime.now(), sys.getdefaultencoding())
sys.setdefaultencoding('utf-8')
print '%s   : 修改当前系统字符集为%s' % (datetime.datetime.now(), sys.getdefaultencoding())
# 备份数据库和仓库文件命令
bak_gitlab_shell = 'gitlab-rake gitlab:backup:create'
print '%s   : 备份数据库和仓库文件命令是 %s' % (datetime.datetime.now(), bak_gitlab_shell)
#执行备份操作
os.system(bak_gitlab_shell)
#备份的路径
base_dir = '/data/backup/'
#gitlab的备份文件名和文件路径，执行备份操作后才能产生文件名
l = os.listdir(base_dir)
#查找最新的备份文件
l.sort(key=lambda fn: os.path.getmtime(base_dir + fn) if not os.path.isdir(base_dir + fn) else 0)
d = datetime.datetime.fromtimestamp(os.path.getmtime(base_dir + l[-1]))
print '%s   : 本地目录中最新的备份文件是： %s\n'% (datetime.datetime.now(), l[-1])
print '%s   : 该文件的最后一次修改时间是： %s\n'% (datetime.datetime.now(),d)
gitlab_file_name = l[-1]
gitlab_file = base_dir + gitlab_file_name
# 统计导出的gitlab备份文件大小
gitlab_file_size = os.path.getsize(gitlab_file)
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
format_file(gitlab_file_size)
print
print '%s   : ........备份结束..........\n'%datetime.datetime.now()
print '---------------------------------------------------------------------\n'
