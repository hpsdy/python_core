#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from pyquery import PyQuery as pq
from urllib import request
from urllib import parse
from urllib.error import HTTPError

class execute(object):
    __slots__ = ('url','file')
    def __init__(self,url):
        self.url = url
        self.file = get_file(url)
    def get_file(self,url,default='index.html'):
        parsed = parse.urlparse(url)


class driver(object):
    count = 0;
    def __init__(self,url):
        self.url = url
        urlparses = parse.urlparse(url)
        self.host = urlparses.netloc.split('@')[-1].split(':')[0]

    def get_page(self):
        pass

dri = driver('http://qinhan:Qh5577325@www.huposedeyue.cn/api/index.html')