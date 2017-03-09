#!/usr/bin/env python
# encoding: utf-8

"""
@description: 多线程处理

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: multifinder.py
@time: 2017/3/9 13:30
"""

import threading

import threadpool

from qqfinder.pth import *
from qqfinder.userfinder import is_not_legal, QQUserFinder

FILE_PATH = '{}/file/'.format(ROOT_PATH)

myUser = QQUserFinder(ldw='1037320121')

pool_size = 100

# cnt = 0


def multi_process():
    datas = load_datas()

    pool = threadpool.ThreadPool(pool_size)
    requests = threadpool.makeRequests(request_item, datas)
    for req in requests:
        pool.putRequest(req)

    pool.poll()
    pool.wait()

    logging.info('task down')


def request_item(uid):
    global cnt

    res = ''
    try:
        # if True:
        #     raise TypeError('hee')
        res = myUser.getUser(uid)
        if is_not_legal(res):
            return

    except Exception as e:
        logging.error("process qq num: [{}] err, {}".format(uid, e))
    if not res:
        logging.error("process qq num: [{}] err, {}".format(uid, None))
        res = '{}{}{}'.format('{"retcode":-1,"result":', uid, '}')

    fname = '{}/{:02d}.txt'.format(FILE_PATH, int(threading.current_thread().name.split('-')[-1]))
    with open(fname, 'a', encoding='utf-8') as fw:
        fw.write('{}\n'.format(res))

    # cnt += 1
    # if cnt % 100 == 0:
    #     logging.info('process qq cnt: {}'.format(cnt))

def load_datas():
    # return [i for i in range(10000, 10000000)]
    return [i for i in range(10000, 15000)]


def main():
    multi_process()


if __name__ == '__main__':
    main()
