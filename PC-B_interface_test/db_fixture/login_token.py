import requests
import time

import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

from db_fixture.common import GlobalVar, Encrypt


class login_token:
    #设置默认为pc-b端接口的访问地址
    def __init__(self,phone=GlobalVar.GVar['user_phone'],password=GlobalVar.GVar['password'],host=GlobalVar.GVar['host']):

        self.co = Encrypt()
        #测试接口地址
        self.host = host
        #获取token
        self.token,self.userID = self.login(phone,self.co.md5Encode(password),host)
        #传输headers，主要是timestamp,token,Signature
        self.headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'X-SNS-ClientType':str(1),
        'X-SNS-Timestamp': str(int(time.time() * 1000)),
        'X-SNS-UserId': self.userId,
        'X-Token': self.token,
        'X-SNS-Signature': self.co.hash1Encode(self.userId + self.token + str(int(time.time() * 1000))),
        }

    def login(self,phone,password,host):
        #访问的端不同，获取token，登录的接口也会不同;app，h5是同一个接口。
            login = {"username":phone,"password":password}
        #配置服务器不请求证书
            r1 = requests.post(host + '/guest/login', verify=False, params=login)
            #获取登录后，json格式的值
            login = r1.json()
            #获取token，userId为sign取值
            try:
                self.token = login['data']['userInfo']['token']
                self.userId = login['data']['userInfo']['userId']
                self.ClientType = str(1)
            except:
                print(login)
            return self.token,self.userId

    def userInfo(self):
        return self.host,self.userId,self.headers

if __name__ == '__main__':
    a = time.time()
    print(login_token().token)
    b = time.time()
    print(b-a)





