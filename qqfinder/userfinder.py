# -*- coding: UTF-8 -*-

'''
    查找QQ用户信息
    暂时未完成用户认证部分，因此目前需要
    1. 自己的QQ号
        qq
    2. skey值
        手动登录QQ空间等，查看网络记录的cookie即可获得
    3. ldw
        意义未知，可以先登录QQ空间，保证cookie中有值，再进入http://find.qq.com进行一次用户查询，查看HTTP的数据段即可获得
    4. 所要查询的用户QQ号
        keyword
'''

import requests
from qqfinder.pth import *
import json
from qqfinder.settings import *
import random

out_file = '{}/file/qq-info.json'.format(ROOT_PATH)


class QQUserFinder():
    '''
        查找用户QQ用户类
    '''
    url = 'http://cgi.find.qq.com/qqfind/buddy/search_v3'

    def __init__(self, keyword=0):
        self.headers = {
            'Host': 'cgi.find.qq.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://find.qq.com/index.html',
            'Origin': 'http://find.qq.com',
        }
        self.post_data = {
            'num': 20,
            'page': 0,
            'sessionid': 0,
            'keyword': keyword,
            'agerg': 0,
            'sex': 0,
            'firston': 1,
            'video': 0,
            'country': 1,
            'province': 11,
            'city': 0,
            'district': 0,
            'hcountry': 1,
            'hprovince': 0,
            'hcity': 0,
            'hdistrict': 0,
            'online': 1,
            # 'ldw': ldw
        }

    def setKeyword(self, keyword=0):
        self.post_data['keyword'] = keyword

    def set_random_user(self):
        random_user = random.choice(users_dict)
        random_user = users_dict[0]
        self.headers['Cookie'] = cookie_format.format(random_user['uid'], random_user['skey'])
        self.post_data['ldw'] = get_ldw(random_user['skey'])

    def fetch_info(self):
        ret = None
        try:
            random_user_agent = random.choice(USER_AGENT_POOL)
            self.headers['User-Agent'] = random_user_agent
            self.set_random_user()

            response = requests.post(self.url, self.post_data, headers=self.headers)
            ret = response.content.decode()
        except Exception as e:
            print('[Error] Query: %d, ErrorMsg: %d %s' % (self.post_data['keyword'], e.args[0], e.args[1]))
        finally:
            return ret

    def getUser(self, uid):
        self.setKeyword(uid)
        info_json = self.fetch_info()
        return info_json


def test():
    myUser = QQUserFinder()

    with open(out_file, 'w', encoding='utf-8') as fw:
        # for i in range(10000, 10000000):
        # for i in range(10004, 10005):
        for i in range(779439458, 779439460):
            try:
                # if True:
                #     raise TypeError('hee')
                res = myUser.getUser(i)

                if is_not_legal(res):
                    continue

            except Exception as e:
                logging.error("process qq num: [{}] err, {}".format(i, e))
            if not res:
                logging.error("process qq num: [{}] err, {}".format(i, None))
                res = '{}{}{}'.format('{"retcode":-1,"result":', i, '}')
            # json.dump(res, fw, ensure_ascii=False)
            fw.write(res)
            fw.write('\n')
            fw.flush()

            if i % 100 == 0:
                logging.info("process qq num: {}".format(i))


# 过滤对方的隐私设置，retcode = 6
def is_not_legal(res):
    if not res:
        return False

    json_data = json.loads(res)
    if json_data['retcode'] == 6:
        return True
    return False


if __name__ == '__main__':
    test()
