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
     'skey': 'Z82Ae3PGUL',
     }, {
        'uid': 779439458,
        'skey': 'ZDl6R0EInV',
    }, {
        'uid': 919230483,
        'skey': 'ZAuvpdz2IK',
    }, {
        'uid': 320621488,
        'skey': 'ZeBAmOuEgQ',
    }, {
        'uid': 424482036,
        'skey': 'Z8Drzc4rC3',
    }, {
        'uid': 275232143,
        'skey': 'ZJxjcC2lK1',
    }, {
        'uid': 207339180,
        'skey': 'ZpvThXejJY',
    }, {
        'uid': 480021292,
        'skey': 'Zo0MFaeiLO',
    }
]

cookie_format = 'uin=o{}; skey={}'


def get_ldw(skey):
    n = 5381
    for i in range(len(skey)):
        n += (n << 5) + ord(skey[i])

    return n & 2147483647


if __name__ == '__main__':
    # skey = 'Z82Ae3PGUL'
    skey = '@rwUbGWWeQ'
    ldw = get_ldw(skey)
    print(ldw)
