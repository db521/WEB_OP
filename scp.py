#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, datetime

host = '192.168.3.168'
print "准备备份到 %s 主机" % host
user = 'root'
# 备份的路径
base_dir = '/usr/local/wiki_home/backups/'
print "需要备份的目录是", base_dir
bakup_file_path = '/data/backup/'
print "备份到远程服务器的目录是：", bakup_file_path
#备份文件名和文件路径
l = os.listdir(base_dir)
#查找最新的备份文件
l.sort(key=lambda fn: os.path.getmtime(base_dir + fn) if not os.path.isdir(base_dir + fn) else 0)
d = datetime.datetime.fromtimestamp(os.path.getmtime(base_dir + l[-1]))
file_name = l[-1]
file = base_dir + file_name
print('最新的备份文件是' + l[-1] + "，修改时间：" + d.strftime("%Y年%m月%d日 %H时%M分%S秒"))
# 统计导出的gitlab备份文件大小
file_size = os.path.getsize(file)
print '%s  : 当前备份的文件大小是 %s' % (datetime.datetime.now(), file_size)


#使用SCP导出到备份服务器
scp_parameter = user + '@' + host + ':'
scp_shell = 'scp ' + base_dir + file_name + ' ' + scp_parameter + bakup_file_path
print "scp执行的完整命令是", scp_shell
print '-------------------------------------------------'
print '................正在传输到远程服务器................'
print
os.system(scp_shell)
print
print '...............传输结束...........................'
print '-------------------------------------------------'