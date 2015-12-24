#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, time, datetime
import sys
from os.path import join

reload(sys)
print '%s  : 系统当前默认字符集是%s' % (datetime.datetime.now(), sys.getdefaultencoding())
sys.setdefaultencoding('utf-8')
print '%s  : 修改当前系统字符集为%s' % (datetime.datetime.now(), sys.getdefaultencoding())
# 待导出数据库信息
db_user = 'admin'
db_passwd = 'admin'
db_type = 'mongodb'
mongo_shell_path = '/usr/local/mongodb/bin/mongodump'
mongo_shell_parameter = ' --authenticationDatabase admin'
print '%s  : 待备份数据库类型 %s' % (datetime.datetime.now(), db_type)
#备份文件命名。
mongo_file_path = db_type + time.strftime('_%H%M%S')
print '%s  : 数据库导出文件名是 %s' % (datetime.datetime.now(), mongo_file_path)
TARGET = 'mongoDB' + time.strftime('%Y%m%d') + '.tar'
print '%s  : 压缩包文件名是 %s' % (datetime.datetime.now(), TARGET)
#备份数据库命令
bak_mongo_shell = mongo_shell_path + ' -o ' + mongo_file_path + ' -u ' + db_user + ' -p=' + db_passwd + mongo_shell_parameter
print '%s  : 备份数据库命令是 %s' % (datetime.datetime.now(), bak_mongo_shell)
#备份压缩命令
tar_command = 'tar -czf %s %s ' % (TARGET, ''.join(mongo_file_path))
print '%s  : 备份压缩命令是 %s' % (datetime.datetime.now(), tar_command)
#执行备份数据库命令
print '-------------------------------------------------'
print '................备份中............................'
print
os.system(bak_mongo_shell)
# 判断导出的mongo文件夹大小，来确定是否执行打包命令
def getdirsize(dir):
    size = 0
    for (root, dirs, files) in os.walk(dir):
        for name in files:
            try:
                size += os.path.getsize(join(root, name))
            except:
                continue
    return size


mongo_file_size = getdirsize(mongo_file_path)
print '%s  : 当前导出的mongodb文件夹大小是 %s' % (datetime.datetime.now(), mongo_file_size)
while True:
    if mongo_file_size == mongo_file_size:
        #如果文件大小相同说明导出到文件已经结束。执行打包命令
        print '%s  : 正在执行压缩命令 %s' % (datetime.datetime.now(), tar_command)
        os.system(tar_command)
        tar_file_size = os.path.getsize(TARGET)
        print '%s  : 当前导出的压缩包大小是 %s' % (datetime.datetime.now(), tar_file_size)
        break
print
print '...............备份结束...........................'
print '-------------------------------------------------'
