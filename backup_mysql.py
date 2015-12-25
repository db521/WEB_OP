#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,time,datetime
import sys
reload(sys)
print '%s  : 系统当前默认字符集是%s' % (datetime.datetime.now(),sys.getdefaultencoding())
sys.setdefaultencoding('utf-8')
print '%s  : 修改当前系统字符集为%s' % (datetime.datetime.now(),sys.getdefaultencoding())
#待导出数据库信息
db_user='root'
db_passwd='daodao@test'
db_dbs='mysql'
print '%s  : 待备份数据库名是 %s'% (datetime.datetime.now(),db_dbs)
#备份文件命名
sql_file_name = db_dbs + time.strftime('_%H%M%S_')+'dump.sql'
TARGET_DIR = '/data/backup/'
print '%s   : 备份到本地 %s目录下 ' % (datetime.datetime.now(), TARGET_DIR)

print '%s  : 数据库导出文件名是 %s'% (datetime.datetime.now(),sql_file_name)
TARGET =TARGET_DIR+time.strftime('%Y%m%d') + '.tar'
print '%s  : 压缩包文件名是 %s'% (datetime.datetime.now(),TARGET)
#备份数据库命令
bak_sql_shell="mysqldump -u" +db_user + " -p"+db_passwd + " " + db_dbs + " > "+TARGET_DIR+sql_file_name
print '%s  : 备份数据库命令是 %s'% (datetime.datetime.now(),bak_sql_shell)
#备份压缩命令
tar_command = 'tar -czf %s %s ' % (TARGET,''.join(TARGET_DIR+sql_file_name))
print '%s  : 备份压缩命令是 %s'% (datetime.datetime.now(),tar_command)
#执行备份数据库命令
print '-------------------------------------------------'
print '................备份中............................'
print
os.system(bak_sql_shell)
#判断导出的SQL文件大小，来确定是否执行打包命令
sql_file_size=os.path.getsize(TARGET_DIR+sql_file_name)
print '%s  : 当前导出的sql文件大小是 %s'% (datetime.datetime.now(),sql_file_size)
while True:
    if sql_file_size==sql_file_size:
        #如果文件大小相同说明导出到文件已经结束。执行打包命令
        print '%s  : 正在执行压缩命令 %s'% (datetime.datetime.now(),tar_command)
        os.system(tar_command)
        tar_file_size=os.path.getsize(TARGET)
        print '%s  : 当前导出的压缩包大小是 %s'% (datetime.datetime.now(),tar_file_size)
        break
print
print '...............备份结束............................'
print '-------------------------------------------------'
