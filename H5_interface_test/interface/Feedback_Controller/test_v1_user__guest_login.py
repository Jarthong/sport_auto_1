import os

import requests

from db_fixture.common import Encrypt, GlobalVar

__author__ = 'huxm855'


def test_v1_user__guest_login():
    ''' 用户登录'''
    base_url =GlobalVar.GVar['host'] + "/v1/user/_guest/login"
    params = {"account": GlobalVar.GVar['user_phone'], "loginPwd": Encrypt().md5Encode(GlobalVar.GVar['password'])}
    r = requests.post(base_url, params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    assert result['data']['userId']==  GlobalVar.GVar['user_id']



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))