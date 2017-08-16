#!/bin/python
#-*- coding:utf-8 -*-
url = 'https://www.amazon.cn/b/?_encoding=UTF8&bbn=658390051&ie=UTF8&node=658810051&ref_=mh_cxrd_sub_658414051_1_image&pf_rd_p=300e9a11-10e8-47af-b1e0-6937d130067c&pf_rd_s=merchandised-search-3&pf_rd_t=101&pf_rd_i=658414051&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=475FTY3VYCD8TT7AT55A&pf_rd_r=475FTY3VYCD8TT7AT55A&pf_rd_p=300e9a11-10e8-47af-b1e0-6937d130067c'
import requests
list = requests.get(url)
with open('./book.txt','ab') as fn:
    print(type(list.text.encode("iso-8859-1").decode('utf-8')))
    fn.write(list.text.encode())