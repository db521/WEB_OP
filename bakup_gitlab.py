#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, datetime
import sys

reload(sys)
print '%s  : 系统当前默认字符集是%s' % (datetime.datetime.now(), sys.getdefaultencoding())
sys.setdefaultencoding('utf-8')
print '%s  : 修改当前系统字符集为%s' % (datetime.datetime.now(), sys.getdefaultencoding())


# 备份数据库和仓库文件命令
bak_gitlab_shell = 'gitlab-rake gitlab:backup:create'
print '%s  : 备份数据库和仓库文件命令是 %s' % (datetime.datetime.now(), bak_gitlab_shell)
print '-------------------------------------------------'
print '................备份中............................'
print
#执行备份操作
os.system(bak_gitlab_shell)
#备份的路径
base_dir = '/var/opt/gitlab/backups/'
#gitlab的备份文件名和文件路径，执行备份操作后才能产生文件名
l = os.listdir(base_dir)
#查找最新的备份文件
l.sort(key=lambda fn: os.path.getmtime(base_dir + fn) if not os.path.isdir(base_dir + fn) else 0)
d = datetime.datetime.fromtimestamp(os.path.getmtime(base_dir + l[-1]))
print('最新的备份文件是' + l[-1] + "，时间：" + d.strftime("%Y年%m月%d日 %H时%M分%S秒"))
gitlab_file_name = l[-1]
gitlab_file = base_dir + gitlab_file_name
# 统计导出的gitlab备份文件大小
gitlab_file_size = os.path.getsize(gitlab_file)
print '%s  : 当前备份的文件大小是 %s' % (datetime.datetime.now(), gitlab_file_size)
print
print '...............备份结束............................'
print '-------------------------------------------------'
