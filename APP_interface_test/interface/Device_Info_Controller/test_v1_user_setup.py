__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import requests


def test_v1_user_setup(login,):
    ''' 用户隐私信息设置'''
    base_url =login[0] + "/v1/user/setup"
    r = requests.put(base_url, headers=login[-1],verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
