#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
邮件发送
'''
from smtplib import SMTP_SSL as smtp
sm = smtp('smtp.qq.com',465)
print(sm)
sm.login('1036474541@qq.com','ruhwxunbmyskbbdf')

#ret=sm.sendmail('1036474541@qq.com','1036474541@qq.com','''From:qinhan\r\nTo:qinhan\r\nSubject:hello world\r\n\r\nthis is a test mail''')
#print(ret)

sm.quit()

from imaplib import IMAP4_SSL as imaps
imap = 'imap.qq.com'
im = imaps(imap)
im.login('1036474541@qq.com','ruhwxunbmyskbbdf')
ret = im.select('INBOX',False)
print(ret)
ret = im.fetch('68','(BODY[TEXT])')
print(ret)