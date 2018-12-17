#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.alog.com"  #设置服务器
mail_user="xxx@xx.com"    #用户名
mail_pass="xxx"   #口令 
 
 
sender = 'yajunwu@alog.com'
receivers = ['51jobwyj@sina.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python 邮件发送测试...</p>
"""

message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2) 
 
try:
    s = smtplib.SMTP_SSL(mail_host,465)
    s.login(mail_user, mail_pass)
    s.sendmail(sender, receivers, message.as_string())

    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
