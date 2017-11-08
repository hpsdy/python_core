#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import io,os
fn = io.StringIO()
html = '''Set-Cookie:a=1;path=/
Set-Cookie:b=2;path=/
Content-Type:text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<h1>hello kity:</h1>
<p>value:{0}</p>
</body>
</html>
'''
import cgi

from os import environ

params = cgi.FieldStorage()
value = params['value'].value
print(html.format(value))
print(environ['HTTP_COOKIE'])
print('file:',params['file'].filename)
print('data:',params['file'].file.read())