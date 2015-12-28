#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, time, datetime
import sys

reload(sys)
print '---------------------------------------------------------------------\n'
print '%s   : ........正在进行备份请稍后..........\n'%datetime.datetime.now()
print '%s   : 系统当前默认字符集是： %s\n' % (datetime.datetime.now(), sys.getdefaultencoding())
sys.setdefaultencoding('utf-8')
print '%s   : 修改当前系统字符集为是： %s\n' % (datetime.datetime.now(), sys.getdefaultencoding())
# 待导出数据库信息
db_type = 'redis'
redis_shell_path = '/usr/local/redis-3.0.5/src/redis-cli'
redis_shell_parameter = ' daodaotest save'
print '%s   : 待备份数据库类型是： %s\n' % (datetime.datetime.now(), db_type)
# 备份文件命名
redis_file_path = '/dump.rdb'
TARGET_DIR = '/data/backup/'
print '%s   : 数据库导出文件名是： %s\n' % (datetime.datetime.now(), redis_file_path)
TARGET = TARGET_DIR+'redis-' + time.strftime('%Y%m%d') + '.tar'
print '%s   : 压缩包文件名是： %s\n' % (datetime.datetime.now(), TARGET)
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
#备份数据库命令
bak_redis_shell = redis_shell_path + '  -p ' + '6379' + ' -a ' + redis_shell_parameter
#备份压缩命令
tar_command = 'tar -czf %s %s ' % (TARGET, ''.join(redis_file_path))
print '%s   : 备份压缩命令是： %s\n' % (datetime.datetime.now(), tar_command)
#执行备份数据库命令
print
os.system(bak_redis_shell)
#判断导出的redis文件大小，来确定是否执行打包命令
redis_file_size = os.path.getsize(redis_file_path)
while True:
    if redis_file_size == redis_file_size:
        #如果文件大小相同说明导出到文件已经结束。执行打包命令
        os.system(tar_command)
        tar_file_size = os.path.getsize(TARGET)
        print '%s   : ........备份成功！！..........\n' %datetime.datetime.now()
        print '%s   : 备份文件为： %s\n' % (datetime.datetime.now(), TARGET)
        format_file(tar_file_size)
        break
print
print '---------------------------------------------------------------------\n'

