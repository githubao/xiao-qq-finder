#!/usr/bin/env python
# encoding: utf-8

"""
@description: 配置文件

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: settings.py
@time: 2017/3/9 14:03
"""

USER_AGENT_POOL = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2725.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.59 QQ/7.9.14308.201 Safari/537.36',
]

users_dict = [
    {'uid': 971230206,
     'skey':'Z82Ae3PGUL',
     'Cookie': 'RK=GT+ufAR6e8; pgv_pvid=5824311650; pt2gguin=o0971230206; ptcz=2638d9b2bc50459c407ebc78db65cf2032904f6c9e617fcca8b4109067c0f7c2; uin=o971230206; skey=Z82Ae3PGUL; itkn=24609040',
     'ldw': 1013161690
     }, {
        'uid': 779439458,
        'skey':'ZDl6R0EInV',
        'Cookie': 'RK=GX0P9Rk+e4; pgv_pvid=3960994630; pt2gguin=o0779439458; ptcz=8b6dfb1adb6ab7e170264682e2b1b64b545053cec8e3ccd248c19eb5ca7e75ab; uin=o779439458; skey=ZDl6R0EInV; itkn=24609040',
        'ldw': 1037320121,
    }
]


def get_ldw(skey):
    n = 5381
    for i in range(len(skey)):
        n += (n << 5) + ord(skey[i])

    return n & 2147483647


if __name__ == '__main__':
    skey = 'Z82Ae3PGUL'
    ldw = get_ldw(skey)
    print(ldw)
