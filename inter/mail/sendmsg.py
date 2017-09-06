#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
邮件发送
'''
from smtplib import SMTP_SSL as smtp
sm = smtp('smtp.qq.com',465)
print(sm)
sm.login('1036474541@qq.com','ruhwxunbmyskbbdf')

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
user = '1036474541@qq.com'
to = user

def mymetamultiparty():
    #meta = MIMEMultipart('alternative')
    meta = MIMEMultipart()
    text = MIMEText('hello world\r\n','plain')
    meta.attach(text)
    html = MIMEText('<html><body><h1>haha</h1></body></html>','html')
    meta.attach(html)
    img = metaimg()
    meta.attach(img)
    return meta
def metaimg():
    fn = 'some.jpg'
    f = open('./timg.jpg','rb')
    data = f.read()
    f.close()
    email = MIMEImage(data,name=fn)
    email.add_header('Content-Disposition','attachment;filename="%s"' % fn)
    return email
msg = mymetamultiparty()
msg['From']=user
msg['To']=to
msg['Subject']='测试'
#ret=sm.sendmail('1036474541@qq.com','1036474541@qq.com','''From:qinhan\r\nTo:qinhan\r\nSubject:hello world\r\n\r\nthis is a test mail''')
ret=sm.sendmail('1036474541@qq.com','1036474541@qq.com',msg.as_string())
print(ret)

sm.quit()

from imaplib import IMAP4_SSL as imaps
imap = 'imap.qq.com'
im = imaps(imap)
im.login('1036474541@qq.com','ruhwxunbmyskbbdf')
ret = im.select('INBOX',False)
print(ret)
ret = im.fetch('68','(BODY[TEXT])')
print(ret)