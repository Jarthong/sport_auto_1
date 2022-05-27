import time

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

from db_fixture.common import GlobalVar, Encrypt

urllib3.disable_warnings(InsecureRequestWarning)


class login_token:
    # 设置默认为pc-b端接口的访问地址
    def __init__(self, phone=GlobalVar.GVar_hq['train_org_phone'], password=GlobalVar.GVar_hq['password'],
                 host=GlobalVar.GVar_hq['host'],ClientType=2):
        self.co = Encrypt()
        # 测试接口地址
        self.host = host
        self.ClientType=ClientType
        # 获取token
        self.token, self.userId = self.login(phone, self.co.md5Encode(password), host)

        # 传输headers，主要是Timestamp，Token，Signature
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'X-SNS-ClientType': str(self.ClientType),
            'X-SNS-Timestamp': str(int(time.time() * 1000)),
            'X-SNS-UserId': self.userId,
            'X-Token': self.token,
            'X-SNS-Signature': self.co.hash1Encode(self.userId + self.token + str(int(time.time() * 1000))),
        }

    def login(self, phone, password, host):
        # 访问的端不同，获取token，登录的接口也会不同；app，h5是同一个接口。
        login = {"account": phone, "loginPwd": password}
        r = requests.post(host + '/v1/user/_guest/login', params=login,verify=False)
        # 获取登录后，json格式的值
        # print(r.json())
        login = r.json()
        # 获取token，userId为sign取值

        self.token = login['data']['token']
        self.userId = login['data']['userId']
        return self.token, self.userId

    def userInfo(self):
        return self.host, self.userId, self.headers


if __name__ == '__main__':
    host, userId, headers = login_token(phone='18770049977',password=GlobalVar.GVar_hxm['passworld']).userInfo()
