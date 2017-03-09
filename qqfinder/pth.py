#!/usr/bin/env python
# encoding: utf-8

"""
@description: 路径配置

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: pth.py
@time: 2017/3/9 11:46
"""

import os
from os.path import abspath, dirname
import logging

FILE_PATH = dirname(abspath(__file__)) + os.sep + 'file' + os.sep
LOG_PATH = dirname(abspath(__file__)) + os.sep + 'log' + os.sep

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='{}/req.log'.format(LOG_PATH),
                    filemode='a',
                    )