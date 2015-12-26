#coding: utf-8
import smtplib,time,os
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
attach_name=time.strftime('%Y%m%d_%H%M%S') + '.tar'#打包后文件名

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
            smtp.sendmail(sender, receiver, msgRoot.as_string())#发送邮件 
            break
        except:
            try:
                smtp.connect(smtpserver)#连接至邮件服务器
                smtp.login(username, password)#登录邮件服务器
            except:
                print "failed to login to smtp server"#登录失败
def tar_logs():
    #备份压缩日志参数
    logs_file_path = '/backup/logs/'#要打包的日志目录
    log_tar_path='/backup/log_tar/'#日志被打包后放的目录
    TARGET =log_tar_path+attach_name#要发送的文件全路径
    tar_command = 'tar -czf %s %s ' % (TARGET, ''.join(logs_file_path))
    os.system(tar_command)
    send_email(MSG,TARGET)
if __name__ == "__main__":
    tar_logs()

