__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests
@pytest.mark.parametrize('thirdType',range(1,4))

def test_v1_user_unbindThirdUser(login,thirdType):
    ''' 解绑第三方用户'''
    base_url =login[0] + "/v1/user/unbindThirdUser"
    params={'thirdType': thirdType}

    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['result']==  '0'
    assert result['msg'] =='成功'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
