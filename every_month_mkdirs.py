#!/usr/bin/python
# -*- coding:utf-8 -*-
import os, datetime,time
print '---------------------------------------------------------------------\n'
host = '192.168.3.168'
print '%s   : 备份服务器IP是： %s\n' % (datetime.datetime.now(), host)
# 备份的路径
path_parmeter1 = '/data/backup/'
path_parmeter2='/'+time.strftime('%Y%m')+"/"
for ip in range(170,187):
    ips=str(ip)#把range里面的int型数字转换为字符串类型方便后面引用
    backup_file_path=path_parmeter1+ips+path_parmeter2
    if not os.path.exists(backup_file_path):#判断当前日期的文件夹是否存在
        os.makedirs(backup_file_path)  # 创建目录
        print "目录创建成功%s\n"%backup_file_path
    else:
        print "目录已经存在%s\n"%backup_file_path
    ip += 1


