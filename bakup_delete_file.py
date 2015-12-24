#! /usr/bin/env python
# -*- coding=utf-8 -*-
import sys
import os
import time, datetime

# 定义需要删除文件的目录
dir = '/data/backup/'
print "要删除的历史备份目录是", dir
# 被删除文件写入日志文件
logdir = '/var/log'
print "删除操作记录的日志目录是：", logdir
logfile = os.path.join(logdir, 'delete.log')
print "删除操作记录的日志名是", logfile
# 获取当前系统python版本
ver = sys.version
ver = ver.split(' ')
ver = ver[0]
print "当前系统的python版本是", ver
# 将"Wed Jul  4 13:25:59 2012"格式的时间转成“2012-07-02 14:50:15”格式的时间
# version是当前系统python版本号
# time是"Wed Jul  4 13:25:59 2012"格式的时间
# 函数返回"2012-07-02 14:50:15"格式的时间
# 时间格式
time_format = "%a %b %d %H:%M:%S %Y"
print "修改系统的日期格式为", time_format
# 取得当前时间
today = datetime.datetime.now()
print "当前时间是", today
# 定义删除周期，这里以2分钟之前的文件被删除为例，可以写小时hours，分钟minutes，日days，周weeks。
four_weeks = datetime.timedelta(minutes=2)
print "2分钟之前是？", four_weeks
# 2分钟之前的日期
four_weeks_ago = today - four_weeks
print "2分钟之前的日期是", four_weeks_ago
# 将时间转成timestamps
four_weeks_ago_timestamps = time.mktime(four_weeks_ago.timetuple())
print "2分钟之前的日期转成时间戳是，", four_weeks_ago_timestamps
# 列出目录中的所有文件
files = os.listdir(dir)
print "目录中的所有文件列表是", files
# 打开要删除的文件日志
fh = open(logfile, "w+")
# 遍历文件，打印出文件的创建时间
for f in files:
    # 忽略掉.开头的文件
    if f.startswith('.'):
        continue
    # 忽略掉当前目录下的目录
    if os.path.isdir(os.path.join(dir, f)):
        continue
    # 获得文件的modify时间，并转换成timestamp格式
    file_timestamp = os.path.getmtime(os.path.join(dir, f))
    # 检查文件的修改时间是否小于2分钟之前的时间戳，如果小于就准备写日志进行删除操作
    if float(file_timestamp) <= float(four_weeks_ago_timestamps):
        #进行写日志操作
        fh.write(str(today) + "\t" + str(file_timestamp) + "\t" + os.path.join(dir, f) + "\n")
        #打印到屏幕上显示即将被删除的文件名和当前时间
        t = os.path.join(dir, f) + "\t" + str(today) + "\t"
        print "即将删除历史备份", t
        os.remove(os.path.join(dir, f))
# 关闭日志文件
fh.close()