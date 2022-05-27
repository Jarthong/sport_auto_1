__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import random

import pytest
import requests


# 经度
@pytest.mark.parametrize('longitude',[random.choice(range(0,180)),None])
# 纬度
@pytest.mark.parametrize('latitude',[random.choice(range(0,90)),None])

def test_v1_user_updateLocal(login,longitude,latitude):
    ''' 更新用户的坐标'''
    base_url =login[0] + "/v1/user/updateLocal"
    params={'longitude':longitude,'latitude':latitude}
    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if longitude==None or latitude==None:
        assert result['result']=='4002'
    else:
        assert result['msg']==  '成功'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
