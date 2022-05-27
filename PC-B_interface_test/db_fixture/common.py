import hashlib
import random
import time
from datetime import timedelta, date
from time import strftime, localtime, time

import requests

"""
随机变量，用户信息，系统访问地址，加密方式
"""

class RandomVar:
    "常用随机变量字段，如name,age,sex,bir,phone,email"

    def random_char_upper(self, num=5):
        '随机5位大写'
        return str(''.join(random.sample(GlobalVar.CHAR_UPPER, num)))

    def random_char_lower(self, num=3):
        '随机5位小写'
        return str(''.join(random.sample(GlobalVar.CHAR_LOWER, num)))

    def random_num(self, start=0, end=99999):
        '随机1-9,取数'
        return random.randint(start, end - 1)

    def random_position_num(self, num=5):
        '随机取5位数'
        return str(''.join(random.sample(GlobalVar.NUM, num)))

    def random_sex(self):
        '随机选择1,2'
        random.choice([1, 2, ])

    def random_phone(self):
        '随机选择号码'
        return str('18770048') + str(random.randint(000, 999))

    def random_birthday(self):
        '随机选择生日'
        return str((random.randint(315504000, 1451577600)) * 1000)

    def random_phone2(self):
        '随机选择号码'
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153",
                   "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    def random_email(self):
        '随机email'
        return str(''.join(random.sample(GlobalVar.CHAR_LOWER, 6)) + '@automation.test')

    def random_imge(self, i=1):
        '随机选择图片'
        return GlobalVar.IMGS[random.randint(i, len(GlobalVar.IMGS))]

    def timeTemp(self, i=0):
        return str(date.today() + timedelta(days=i))

    def date(self):
        year = strftime("%Y", localtime())
        mon = strftime("%m", localtime())
        day = strftime("%d", localtime())
        hour = strftime("%H", localtime())
        min = strftime("%M", localtime())
        sec = strftime("%S", localtime())
        timeTemp = int(time.time() * 1000)
        now = strftime("%Y-%m-%d %H:%M:%S")
        return now, timeTemp


class Encrypt:
    def hash1Encode(self, codeStr):
        hashobj = hashlib.sha1()
        hashobj.update(codeStr.encode('utf-8'))
        return hashobj.hexdigest()

    def md5Encode(self, codeStr):
        m = hashlib.md5()
        m.update(codeStr.encode('utf-8'))
        return m.hexdigest()


class GlobalVar:
    CHAR_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXY'
    NUM = '0123456789'
    CHAR_LOWER = 'abcdefghijklmnopqrstuvwxy'
    IMGS = [
        "http://file.htxk.com/f/20170822/cmsweb/article/i/a1fc644f6ae94b1da682cbd9487ebcec.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/b5685534546148709e17f298b31530bb.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/0f24732e7b3f4617bd35c389a6849237.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/4e2afa95b58240ae82af02aa8d550fd6.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/f2d20dcd4c204d488329c7d796d6c974.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/5df35603df38490385ca3c789a07a405.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/83cf6862392441a9be536a984511e6c2.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/a2907ca9f30341b0bff0c8ba76136a5a.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/fb7cecc8f956448d878f52d9a5884c72.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/93f27020077b44d8b96a2785dc706a3e.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/4fd5a039a41e49588847cb5168165f11.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/77b3d66ee4bc47c5978efeca619fae10.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/4cb6d959ec874023b41496c4429e7b1f.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/d6017d3f74e94e3597b3fec8e43744f9.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/5d8ce4f57d894b60865450fe74583614.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/ba9933245ba448ca934eb3815689b191.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/d3754aa294fd4081ae949c08e13d07ed.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/e5d1427d9b1044c787158e3b67fce34f.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/779e9fb630844efcb4eda2282816e674.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/806fa7e3266648a6a05f8c76a542d04d.jpg",
        "http://file.htxk.com/f/20170822/cmsweb/article/i/9bc95d1d0e104d819505e9f85216186e.jpg",
    ]
    # 设置培训组织ID,赛事组织ID,登录名ID,密码,默认登录HOST
    # TRAIN_ORG_PHONE, MATCH_ORG_PHONE, PHONE, PASSWORD, HOST,
    GVar = {'user_phone': '18770048014',
            'user_id': 'hhly014',
            'password': '123456abc',
            'train_password': '123456a',
            'train_org_phone': '13885980513',
            'train_org_phone2': '18770048010',
            'train_org_userId': 'seedp543381',
            'match_org_phone': '18770049977',
            'match_org_userId': 'seedp50',
            'host': 'https://org.htxksport.com/api',
            'pcCHost': 'https://www.htxksport.com/',
            'authOrgIds':['seedp50','seedp543381']
            }

    GVar_hq = {'user_phone': '13027766155',
               'user_phone2':'18681537823',
            'user_id': 'seedp546981',
            'user_id2':'seedp543681',
            'password': '123456a',
            'host': 'https://org.htxksport.com/api',
            }
if __name__ == '__main__':
    login = {"account": 18770049977, "loginPwd": Encrypt().md5Encode('123456abc')}
    r = requests.post('https://org.htxksport.com/api' + '/v1/user/_guest/login', params=login,verify=False)
    print(r.json())