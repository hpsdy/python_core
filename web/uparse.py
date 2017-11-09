#!/usr/bin/env python3
# -*- coding:utf-8 -*-
a=1000
'''
from urllib import request
from urllib import parse

url = 'http://yf-rdqa04-dev150-qinhan.epc.baidu.com:8899/fuwuui/store/svindex'
data = {
    'clientType': 2,
    'from': 'nmplusmis',
}
data = parse.urlencode(data).encode()
headers = {
    'Cookie': 'flag=001; access_log=28f3851f342503d46d95364bd22d11ed; bn_na_copid=da427e89a09de2b5fc2fc5fbe0a8ab61; BAIDUID=5EFE4E18D634FF03D658D42B1B727D37:FG=1; areaCode=1400320000; Hm_lvt_a028c07bf31ffce4b2d21dd85b0b8907=1503919556,1505121140,1506330552; BDUSS=czUG85RXJXcVRCSHZHNTNUdUJPMHBFZlU3RlhQeVg0QUY0VjVpcHliRDNGLU5aTVFBQUFBJCQAAAAAAAAAAAEAAABRouQ-cWluaGFux9gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPeKu1n3irtZR0; __cas__st__316=81eca006a28ea88e3862ddfa6eb8f652cc71ca52a712bf2ff089274071b87623dfa68a1515375e0e3c1de8e0; __cas__id__316=8753583; __cas__rn__=0; mcttk=7280dab165cf5e23b7bc96bc74aca278; JSESSIONID=D4CCCA926E7FEC4BC93F0A23097A3C3D; PMS_JT=%28%7B%22s%22%3A1508314575127%2C%22r%22%3A%22https%3A//mct.y.nuomi.com/index%3Fpage%3Dtrue%22%7D%29; Hm_lvt_cc68bb575a974efd0d14798d876e6880=1505982762,1507799532,1508312862; Hm_lpvt_cc68bb575a974efd0d14798d876e6880=1508314576',
}
req = request.Request(url, data=data, headers=headers)
print(req)
fn = request.urlretrieve(req,filename='1.json')
print(fn)

'''
