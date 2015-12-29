#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, errno
import datetime, time

print '---------------------------------------------------------------------\n'
print '%s   : ........正在进行备份请稍后..........\n'%datetime.datetime.now()
SOURCE = ['/deploy/']
print '%s   : 即将备份的目录是： %s\n'% (datetime.datetime.now(), SOURCE)
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
#执行压缩命令
if os.system(tar_command) ==0:
    print '%s   : ........备份成功！！..........\n' %datetime.datetime.now()
    print '%s   : 备份文件为： %s\n' % (datetime.datetime.now(), TARGET)
else:
    print '%s   : ........备份失败！！ ..........\n' % (datetime.datetime.now())
os.system('sleep 2')
print
print '---------------------------------------------------------------------\n'

