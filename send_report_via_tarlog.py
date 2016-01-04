#!/usr/bin/python
# -*- coding:utf-8 -*-
import smtplib,time,os,datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#基本参数部分
sender = 'zhangdelong@dongdao.net'#发件人地址
receiver = 'zhangdelong@dongdao.net','lufanglong@dongdao.net','wangpeng@dongdao.net'#收件人地址列表
#receiver='zhangdelong@dongdao.net','745887513@qq.com'
smtpserver = 'smtp.exmail.qq.com'#邮件服务器
username = 'zhangdelong@dongdao.net'#用户名
password = '131415aA'#密码
smtp = smtplib.SMTP()
#报表日志路径
log_parameter1=time.strftime('_%Y%m%d')
log_parameter2='.log'
log_para=log_parameter1+log_parameter2
log_tar_path='/backup/log_tar/'#日志被打包后放的目录
report=log_tar_path+'report'+log_para
#下面为报表日志参数部分
f = open(report, 'rb')
mail_body = f.read()#打开后，进行读取
f.close()#读取完成后关闭文件
MSG = MIMEText(mail_body, _subtype='plain', _charset='utf-8')# 把邮件的正文内容进行格式化，选择类型是HTML格式，编码采用utf-8
attach_name='todaylogs'+time.strftime('%Y%m%d_%H%M%S') + '.tar'#打包后文件名
#备份压缩日志参数
#下面是目录列表太多
log_folder='/backup/logs'
log_parameter1=time.strftime('_%Y%m%d')
log_parameter2='.log '
log_para=log_parameter1+log_parameter2
log_tar_path='/backup/log_tar/'#日志被打包后放的目录
#------------------------------------------
log_186_backup_folder=log_folder+'/186/backup_folder'
log_186_scp_folder   =log_folder+'/186/scp_folder'
log_185_backup_folder=log_folder+'/185/backup_folder'
log_185_scp_folder   =log_folder+'/185/scp_folder'
log_184_backup_folder=log_folder+'/184/backup_folder'
log_184_scp_folder   =log_folder+'/184/scp_folder'
log_183_backup_folder=log_folder+'/183/backup_folder'
log_183_scp_folder   =log_folder+'/183/scp_folder'
log_182_backup_mysql =log_folder+'/182/backup_mysql'
log_182_scp_folder   =log_folder+'/182/scp_folder'
log_181_backup_mysql =log_folder+'/181/backup_mysql'
log_181_scp_folder   =log_folder+'/181/scp_folder'
log_178_backup_mongo =log_folder+'/178/backup_mongo'
log_178_scp_folder   =log_folder+'/178/scp_folder'
log_177_backup_redis =log_folder+'/177/backup_redis'
log_177_scp_folder   =log_folder+'/177/scp_folder'
log_175_backup_folder=log_folder+'/175/backup_folder'
log_175_scp_folder   =log_folder+'/175/scp_folder'
log_174_backup_nexus =log_folder+'/174/backup_nexus'
log_174_backup_mysql =log_folder+'/174/backup_mysql'
log_174_scp_nexus    =log_folder+'/174/scp_nexus'
log_174_scp_testlink =log_folder+'/174/scp_testlink'
log_173_backup_gitlab=log_folder+'/173/backup_gitlab'
log_173_scp_folder   =log_folder+'/173/scp_folder'
log_172_scp_jira     =log_folder+'/172/scp_jira'
log_172_scp_wiki     =log_folder+'/172/scp_wiki'
log_170_backup_mysql =log_folder+'/170/backup_mysql'
log_170_scp_folder   =log_folder+'/170/scp_folder'
log_167_send_report_via_tarlog=log_folder+'/167/send_report_via_tarlog'

#------------------------------------------
find_today_logs=[log_186_backup_folder,log_186_scp_folder,log_185_backup_folder,log_185_scp_folder,log_184_backup_folder,
                 log_184_scp_folder,log_183_backup_folder,log_183_scp_folder,log_182_backup_mysql,log_182_scp_folder,
                 log_181_backup_mysql,log_181_scp_folder,log_178_backup_mongo,log_178_scp_folder,log_177_backup_redis,
                 log_177_scp_folder,log_175_backup_folder,log_175_scp_folder,log_174_backup_nexus,log_174_backup_mysql,
                 log_174_scp_nexus,log_174_scp_testlink,log_173_backup_gitlab,log_173_scp_folder,log_172_scp_jira,
                 log_172_scp_wiki,log_170_backup_mysql,log_170_scp_folder,log_167_send_report_via_tarlog+log_para]
#------------------------------------------
def send_email(file_name):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = "服务器备份日报"+time.strftime('%Y%m%d') #主题
    msgRoot['From'] = 'zhangdelong@dongdao.net'#发件人
    msgRoot['To'] = ",".join(receiver)#收件人
    msgRoot.attach(MSG)#添加邮件正文，正文在前面参数部分
    att = MIMEText(open('%s'%file_name, 'rb').read(), 'base64', 'utf-8')#添加附件
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s"'%attach_name
    msgRoot.attach(att)
    while 1:#持续尝试发送，直到发送成功
        try:
            print '%s   : ........邮件发送成功..........\n'%datetime.datetime.now()
            print '%s   : 正在发送至%s\n'%(datetime.datetime.now(),receiver)
            smtp.sendmail(sender, receiver, msgRoot.as_string())#发送邮件
            break
        except:
            try:
                smtp.connect(smtpserver)#连接至邮件服务器
                smtp.login(username, password)#登录邮件服务器
            except:
                print "failed to login to smtp server"#登录失败
    print '%s   : ........邮件发送成功..........\n'%datetime.datetime.now()
def tar_logs():
    TARGET =log_tar_path+attach_name#要发送的文件全路径
    #tar_command = 'tar -czf %s %s ' % (TARGET,' '.join(find_today_logs+log_para))
    tar_command = 'tar -czf %s %s ' % (TARGET,log_para.join(find_today_logs))
    os.system(tar_command)
    send_email(TARGET)
if __name__ == "__main__":
    tar_logs()


