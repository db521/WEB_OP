#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, errno
import datetime, time

print '---------------------------------------------------------------------\n'
time1=datetime.datetime.now()#增加统计时长计算，和脚本最后面进行相减操作，计算出脚本执行时长
print '%s   : ........正在进行备份请稍后..........\n'%datetime.datetime.now()
SOURCE = ['/deploy/']
print '%s   : 即将备份的目录是： %s\n'% (datetime.datetime.now(), SOURCE)
if not os.path.exists(SOURCE[0]):
    print '%s   : 即将备份的目录：%s不存在！！ \n'% (datetime.datetime.now(), SOURCE)
TARGET_DIR = '/data/backup/'+ time.strftime('%Y%m') + "/"#本地备份到/data/backup/201512/目录下
print '%s   : 即将备份到 %s 目录下\n' % (datetime.datetime.now(), TARGET_DIR)
NAME_FILE = 'deploy' + time.strftime('-%H%M%S')
print '%s   : 即将生成的备份文件名是： %s\n' % (datetime.datetime.now(), NAME_FILE)
TARGET = TARGET_DIR + NAME_FILE + '.tar'
tar_command = 'tar -cvzf %s %s ' % (TARGET, ' '.join(SOURCE))
print '%s   : 压缩命令是： %s\n' % (datetime.datetime.now(), tar_command)
#判断/data/backup/是否存在
def mkdir_p(TARGET_DIR):
    try:
        if not os.path.exists(TARGET_DIR):
            os.makedirs(TARGET_DIR)  # 等同于 makdir -p /data/backup/
            print '%s   : backup备份目录创建成功： %s\n' % (datetime.datetime.now(), TARGET_DIR)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(TARGET_DIR):
            pass
        else:
            raise
mkdir_p(TARGET_DIR)
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
#执行压缩命令
if os.system(tar_command) ==0:
    print '%s   : ........备份成功！！..........\n' %datetime.datetime.now()
    print '%s   : 备份文件为： %s\n' % (datetime.datetime.now(), TARGET)
    file_size = os.path.getsize(TARGET)#使用这个方法获取目标目录下的文件大小
    format_file(file_size)#使用format函数格式化输出文件大小为正常人方式
else:
    print '%s   : ........备份失败！！ ..........\n' % (datetime.datetime.now())
os.system('sleep 2')
time2=datetime.datetime.now()
time3=time2-time1
print '此次备份总共耗时:',time3#计算出脚本的执行时长
print
print '---------------------------------------------------------------------\n'

