#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib import request
from urllib import parse
from urllib.error import HTTPError, URLError

host = 'http://www.huposedeyue.cn/api/index.php'
login = 'qinhan'
pwd = 'Qh5577325'
realm = 'pwd must need:'
print('.'.join(parse.urlparse(host)[1].split('.')[-2:]))


def handler_version(url):
    defAuth = request.HTTPPasswordMgrWithDefaultRealm()
    defAuth.add_password(None, 'www.huposedeyue.cn', login, pwd)
    checkAuth = request.HTTPBasicAuthHandler(defAuth)
    cookies = request.Request.add_header('');
    opener = request.build_opener(checkAuth)
    request.install_opener(opener)
    return url


def requset_version(url):
    from base64 import b64encode
    req = request.Request(url)
    authstring = b64encode(('%s:%s' % (login, pwd)).encode())[:-1]
    print(authstring)
    req.add_header('Authorization', 'Basic %s' % authstring.decode())
    return req


hurl = handler_version(host)
f = request.urlretrieve('http://www.huposedeyue.cn/api/index.php','abc')
print(f)


