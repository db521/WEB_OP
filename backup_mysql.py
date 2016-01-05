#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,time,datetime
import sys,subprocess

reload(sys)
print '---------------------------------------------------------------------\n'
time1=datetime.datetime.now()#增加统计时长计算，和脚本最后面进行相减操作，计算出脚本执行时长
print '%s   : ........正在进行备份请稍后..........\n'%datetime.datetime.now()
print
print '%s  : 系统当前默认字符集是： %s\n' % (datetime.datetime.now(),sys.getdefaultencoding())
sys.setdefaultencoding('utf-8')
print '%s  : 修改当前系统字符集为： %s\n' % (datetime.datetime.now(),sys.getdefaultencoding())
#待导出数据库信息
db_user='root'
db_passwd='daodao@test'
db_dbs='mysql'
print '%s  : 待备份数据库类型是： %s\n'% (datetime.datetime.now(),db_dbs)
#备份文件命名
sql_file_name = db_dbs + time.strftime('-%H%M%S-')+'dump.sql'
print '%s  : 数据库导出文件名是 %s\n'% (datetime.datetime.now(),sql_file_name)
TARGET_DIR = '/data/backup/'+time.strftime('%Y%m')+'/'
print '%s   : 备份到本地 %s目录下 \n' % (datetime.datetime.now(), TARGET_DIR)
#判断/data/backup/日期目录是否存在
if not os.path.exists(TARGET_DIR):#判断当前日期的文件夹是否存在
    os.makedirs(TARGET_DIR)  # 创建目录
    print '%s   : 当前日期的目录创建成功： %s\n' % (datetime.datetime.now(), TARGET_DIR)
TARGET =TARGET_DIR+db_dbs+'-'+time.strftime('%Y%m%d') + '.tar'
#备份数据库命令
bak_sql_shell="mysqldump -u" +db_user + " -p"+db_passwd + " " + db_dbs + ' --verbose '+ " > "+TARGET_DIR+sql_file_name
#备份压缩命令
tar_command = 'tar -cvzf %s %s ' % (TARGET,''.join(TARGET_DIR+sql_file_name))
print '%s  : 备份压缩命令是： %s\n'% (datetime.datetime.now(),tar_command)
#执行备份数据库命令
print
try:
    retcode =subprocess.call(bak_sql_shell, shell=True)
    if retcode < 0:
        print >>sys.stderr, "sql导出子进程被终止，返回码是", -retcode
        print '%s   : ........sql导出备份失败！！..........\n' %datetime.datetime.now()
    if retcode ==0:
        print '%s   : ........sql导出成功！！..........\n' %datetime.datetime.now()
    else:
        print >>sys.stderr, "sql导出子进程返回码是", retcode
        print '%s   : ........sql导出备份失败！！..........\n' %datetime.datetime.now()
except OSError as e:
    print >>sys.stderr, "sql导出错误信息:", e
    print '%s   : ........sql导出备份失败！！..........\n' %datetime.datetime.now()
#判断导出的SQL文件大小，来确定是否执行打包命令
sql_file_size=os.path.getsize(TARGET_DIR+sql_file_name)
#用正常人方式显示文件大小
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
if retcode==0 and sql_file_size==sql_file_size:#条件1：如果导出SQL备份成功，再执行压缩备份，否则不备份；条件2：如果文件大小相同说明导出到文件已经结束。执行打包命令
    try:
        retcode1 =subprocess.call(tar_command, shell=True)
        if retcode1 < 0:
            print >>sys.stderr, "tar导出子进程被终止，返回码是", -retcode1
            print '%s   : ........tar备份失败！！..........\n' %datetime.datetime.now()
        if retcode1 ==0:
            print '%s   : ........tar备份成功！！..........\n' %datetime.datetime.now()
            tar_file_size=os.path.getsize(TARGET)
            format_file(tar_file_size)
            print '%s   : 备份文件为： %s\n' % (datetime.datetime.now(), TARGET)
        else:
            print >>sys.stderr, "tar导出子进程返回码是", retcode1
            print '%s   : ........tar备份失败！！..........\n' %datetime.datetime.now()
    except OSError as e:
        print >>sys.stderr, "tar导出错误信息:", e
        print '%s   : ........tar备份失败！！..........\n' %datetime.datetime.now()
time2=datetime.datetime.now()
time3=time2-time1
print '此次备份总共耗时:',time3#计算出脚本的执行时长
print '---------------------------------------------------------------------\n'
