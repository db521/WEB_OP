# -*- coding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
# 发件人和收件人
fromaddr = 'zhangdelong@dongdao.net'
toaddrs = '745887513@qq.com'
username = 'zhangdelong@dongdao.net'
password = '131415aA'
#发送邮件函数
def sendmail(msg):
    #以下是完整的发送邮件模块
    server = smtplib.SMTP('smtp.exmail.qq.com')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()


#发送的报告路径和读取内容后，进行发送
def sendreport():
    #报告的路径和文件名
    f = open('D:\\sendmail_test\\2015-11-12 10_19_08result -1.html', 'rb')
    #打开后，进行读取
    mail_body = f.read()
    #读取完成后关闭文件
    f.close()
    # 把邮件的正文内容进行格式化，选择类型是HTML格式，编码采用utf-8
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    #发送的邮件标题，发件人，收件人等信息
    msg['Subject'] = 'I miss you'
    msg['From'] = 'zhangdelong@dongdao.net'
    msg['To'] = '745887513@qq.com'
    #调用发送邮件函数
    sendmail(msg)

# 如果当前模块是入口模块，执行发送报告操作
if __name__ == "__main__":
    sendreport()
