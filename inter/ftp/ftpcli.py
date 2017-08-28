#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import ftplib
import os
f = ftplib.FTP('ftp.huposedeyue.cn')
f.set_debuglevel(2)
f.login('work','Qh5577325')
f.set_pasv(0)
files=f.nlst()
print('dir:',files)
for file in files:
    file = './'+file
    tmp = open(file,'wb').write
    f.retrbinary('RETR '+file,tmp,1024)
