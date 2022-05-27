__author__ = 'huxm855'
import os

import pytest
import requests

from db_fixture.common import RandomVar

ra = RandomVar()
var = [1, 2, 0, -1]


@pytest.mark.parametrize('sex', var)
@pytest.mark.parametrize('age', var)
def test_v1_user__userInfo(login, sex, age):
    ''' 修改用户信息'''
    base_url = login.host + "/v1/user/_userInfo"
    params = {'sex': sex, 'email': ra.random_email(), 'age': age}
    r = requests.put(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if sex in var[2:] or age in var[3:]:
        assert result['msg'] in ('性别输入不正确!', '年龄输入不正确!')
    else:
        assert result['msg'] in ('成功', '认证组织IP,不能修改昵称')


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
