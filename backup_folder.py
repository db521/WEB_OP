#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, errno
import datetime, time


def backup():
    print '-------------------------------------------------'
    print ".............正在进行备份请稍后 ...................."
    print
    SOURCE = ['/usr/local/tomcat7/']
    print '%s   : 即将备份的目录是 %s ' % (datetime.datetime.now(), SOURCE)
    TARGET_DIR = '/data/backup/'
    print '%s   : 备份到本地 %s目录下 ' % (datetime.datetime.now(), TARGET_DIR)
    NAME_FILE = 'tomcat7' + time.strftime('_%H%M%S')
    print '%s   : 即将备份的文件夹是 %s ' % (datetime.datetime.now(), NAME_FILE)
    today = time.strftime('%Y%m%d')
    print '%s   : 生成当前系统日期的目录 %s ' % (datetime.datetime.now(), today)
    TARGET = TARGET_DIR + time.strftime('%Y%m%d') + "/" + NAME_FILE + '.tar'
    print '%s   : 备份后的压缩包是 %s ' % (datetime.datetime.now(), TARGET)
    #zip_command = "zip -qr '%s' %s " % (TARGET, ' '.join(SOURCE))
    tar_command = 'tar -cvzf %s %s ' % (TARGET, ' '.join(SOURCE))
    print '%s   : 压缩命令是 %s ' % (datetime.datetime.now(), tar_command)
    #Scripts Exec process Start
    print
    #Judge TARGET_DIR
    def mkdir_p(TARGET_DIR):
        try:
            if not os.path.exists(TARGET_DIR):
                os.makedirs(TARGET_DIR)  # == makdir -p /data/backup/
                print '%s   : backup备份目录创建成功 %s' % (datetime.datetime.now(), TARGET_DIR)
        except OSError as exc:  # Python >2.5 (except OSError, exc: for Python <2.5)
            if exc.errno == errno.EEXIST and os.path.isdir(TARGET_DIR):
                pass
            else:
                raise

    mkdir_p(TARGET_DIR)
    #Judge today DIR
    if not os.path.exists(today):
        os.mkdir(today)  # make DIRectory
        print '%s   : 当前日期的目录创建成功 %s' % (datetime.datetime.now(), today)
    #Exec Zip Command to Dir or file
    if os.system(tar_command) == 0:
        print '%s   : 备份成功！！ %s' % (datetime.datetime.now(), TARGET)
    else:
        print '备份失败!'
        print '%s   : 备份失败!' % (datetime.datetime.now())
    os.system('sleep 2')
    print
    print '--------------- 备份脚本执行完毕 ------------------'


backup()
