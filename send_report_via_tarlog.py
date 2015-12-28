#!/usr/bin/python
# -*- coding:utf-8 -*-
import smtplib,time,os,datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#基本参数部分
sender = 'zhangdelong@dongdao.net'#发件人地址
receiver = 'zhangdelong@dongdao.net','lufanglong@dongdao.net','wangpeng@dongdao.net'#收件人地址列表
smtpserver = 'smtp.exmail.qq.com'#邮件服务器
username = 'zhangdelong@dongdao.net'#用户名
password = '131415aA'#密码
smtp = smtplib.SMTP()
MSG="内容见附件，请注意查收！"#要发送的文字
attach_name='todaylogs'-time.strftime('%Y%m%d_%H%M%S') + '.tar'#打包后文件名

def send_email(msg,file_name):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = "服务器备份日报"+time.strftime('%Y%m%d') #主题
    msgRoot['From'] = 'zhangdelong@dongdao.net'#发件人
    msgRoot['To'] = ",".join(receiver)#收件人
    msgText = MIMEText('%s'%msg,'html','utf-8')#你所发的文字信息将以html形式呈现
    msgRoot.attach(msgText)
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
    #备份压缩日志参数
    find_today_logs='find /backup/logs/ -mmin -540'#查找当天产生的日志,此处的参数是查找540分钟以内被修改的文件，也就是9小时以内。从00:00-9:00之间
    log_tar_path='/backup/log_tar/'#日志被打包后放的目录
    TARGET =log_tar_path+attach_name#要发送的文件全路径
    tar_command=find_today_logs+' -exec'+' tar -czf '+TARGET +' {} \;'
#这句命令的原型是：find /backup/logs/ -mmin -540  -exec tar -czf /backup/log_tar/todaylogs-20151228.tar {} \;
#find . -name "*something*"  找出所有名字包含something的文件
#-exec 执行后面的命令， action 某个命令名，就是例子中的tar， {}是find的结果集合，
#somearguments ， 命令需要的参数，就是例子中的'-czf /backup/log_tar/todaylogs-20151228.tar '，\; 结束命令
    os.system(tar_command)
    send_email(MSG,TARGET)
if __name__ == "__main__":
    tar_logs()

