
__author__ = 'huxm855'
import os
import pytest
import re
import requests



def test_user_exit(login,):
    ''' 登出'''
    base_url =login.host + "/user/exit"
    r = requests.get(base_url, headers=login.headers,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    assert result['data']==  '登出成功'



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))