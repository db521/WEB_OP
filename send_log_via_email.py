#!/usr/bin/env python3    
# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 发件人和收件人
fromaddr = 'zhangdelong@dongdao.net'
toaddrs = '745887513@qq.com'
username = 'zhangdelong@dongdao.net'
password = '131415aA'
#邮件的基本参数，发件人、收件人、标题
msg = MIMEMultipart('related')
msg['Subject'] = 'I miss you'
msg['From'] = 'zhangdelong@dongdao.net'
msg['To'] = '745887513@qq.com'

#构造附件    
att = MIMEText(open('d:\\sendmail_test\\a.log', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="a.log"'
msg.attach(att)


def sendmail(msg):
    #以下是完整的发送邮件模块
    server = smtplib.SMTP('smtp.exmail.qq.com')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()

# 如果当前模块是入口模块，执行发送邮件操作并把附件一块发送
if __name__ == "__main__":
    sendmail(msg)

