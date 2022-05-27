import hashlib
import random
import time
from datetime import timedelta, date
from time import strftime, localtime, time

"""
随机变量，用户信息，系统访问地址，加密方式
"""


class RandomVar:
    "常用随机变量字段，如name,age,sex,bir,phone,email"

    def random_char_upper(self, num=5):
        '随机5位大写'
        return str(''.join(random.sample(GlobalVar.CHAR_UPPER, num)))


    def random_num(self, start=0, end=99999):
        '随机1-9,取数'
        return random.randint(start, end - 1)

    def random_email(self):
        '随机email'
        return str(''.join(random.sample(GlobalVar.CHAR_LOWER, 6)) + '@automation.test')
    def random_az(self):
        '随机选择字母a-z'
        return chr(random.randint(97, 122))
    def random_phone(self):
        '随机选择号码'
        return str('18770048') + str(random.randint(000, 999))
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
    GVar_hq = {'train_org_phone': '18681537823',
               'password_ymm': 'a11111',
               "match_org_phone": '15566669923',
               'password': '123456a',
               'host': 'https://app.hhlysport.com/api',
               'train_org_id': 'seedp543681',
               'user_id': 'seedp543681',
               'match_org_id': 'seedp10',
               'phone_2': '13027766155',
               'password_2': '123456a'
               }
    GVar_hxm = {
        # 'user_phone': '18770048016',
        'user_phone': '18770049977',
            'user_id': 'seedp50',
        # 'user_id': 'hhly016',
        'orgId': '34413',
        'passworld': '123456abc',
        'host': 'https://app.hhlysport.com/api',
        'host_h5': 'https://m.hhlysport.com/api',
        'user_phone2': '18770048016',
    }
    GVar_chh = {'user_phone': '18600000002',
                'user_password': '123456',
                'host': 'https://app.hhlysport.com/api',
                'userid': 'seedp49'
                }

    USERIDS = (GVar_hq['match_org_id'], GVar_hq['user_id'])
    USERIDS_YMM = (GVar_hq['user_id'])
    ORG_USERIDS = (GVar_hq['match_org_id'],GVar_hq['train_org_id'])


if __name__ == '__main__':
    print(Encrypt().md5Encode(GlobalVar.GVar_hxm['passworld']))
