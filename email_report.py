#!/usr/bin/python
# -*- coding:utf-8 -*-
import time,re
#基础参数部分
log_folder='/backup/logs'#基础目录
log_parameter1=time.strftime('_%Y%m%d')
log_parameter2='.log'
log_para=log_parameter1+log_parameter2
log_tar_path='/backup/log_tar/'#日志被打包后放的目录
report=log_tar_path+'report'+log_para
text=['备份失败','备份文件为','当前备份的文件大小是','待备份数据库类型是'
    ,'即将备份的目录是','待备份数据库名是','待备份数据类型是','本地目录中最新的备份文件是']#定义要查找的多个字符串,增加jira和wiki的完整文件路径。
#------------------------------------------
log_186_backup_folder=log_folder+'/186/backup_folder'
log_185_backup_folder=log_folder+'/185/backup_folder'
log_184_backup_folder=log_folder+'/184/backup_folder'
log_183_backup_folder=log_folder+'/183/backup_folder'
log_182_backup_mysql =log_folder+'/182/backup_mysql'
log_181_backup_mysql =log_folder+'/181/backup_mysql'
log_178_backup_mongo =log_folder+'/178/backup_mongo'
log_179_backup_mongo =log_folder+'/179/backup_mongo'#增加179备份
log_177_backup_redis =log_folder+'/177/backup_redis'
log_175_backup_folder=log_folder+'/175/backup_folder'
log_174_backup_nexus =log_folder+'/174/backup_nexus'
log_174_backup_mysql =log_folder+'/174/backup_mysql'
log_173_backup_gitlab=log_folder+'/173/backup_gitlab'
log_172_scp_jira     =log_folder+'/172/scp_jira'
log_172_scp_wiki     =log_folder+'/172/scp_wiki'
log_170_backup_mysql =log_folder+'/170/backup_mysql'
find_today_logs=[log_186_backup_folder,log_185_backup_folder,log_184_backup_folder,
                log_183_backup_folder,log_182_backup_mysql,log_181_backup_mysql,
                log_178_backup_mongo,log_179_backup_mongo,log_177_backup_redis,log_175_backup_folder,
                log_174_backup_nexus,log_174_backup_mysql,log_173_backup_gitlab,
                log_172_scp_jira,log_172_scp_wiki,log_170_backup_mysql]
#定义日志输出函数，输出一个表格日志
def every_log_file():
    file_object=open(report,'w')#写一个总结报表到新的日志文件中
    file_object.write('  今天的日期是%s,今天的备份日志报表如下所示.\n更多的详细信息请参见附件日志文件!\n'%time.strftime('%Y年%m月%d日'))
    for today_log in find_today_logs:#查找每一个待查的日志文件名
        ip=re.findall(r'\d{3}',today_log)#正则匹配文件夹路径里面的纯数字部分，要求是3位数字，这里是取到服务器的IP
        file_object.write('-------------------------%s服务器----------------------------------\n'%ip)
        file_object.write('\n')#换行
        file_context = open(today_log+log_para)#打开文件进行读取，读取每一个日志文件
        for line in file_context:#定义line变量读取文件每一行内容
            for text_str in text:#定义待查询的字符串每一个元素
                if not line.find(text_str)== -1:#查找日志文件每一行里面是否有存在的待查字符串
                    file_object.write(line)#如果该行有待查的字符串，写入新的日志文件
        file_object.write('\n') #换行
        file_context.close()#关闭日志文件
    file_object.close()#关闭总结报表日志文件
every_log_file()#调用总结报表函数
