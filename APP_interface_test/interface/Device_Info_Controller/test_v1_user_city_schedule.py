__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests


@pytest.mark.parametrize('date', [None, '2018-1'])
def test_v1_user_city_schedule(login, date):
    ''' 用户的日程'''
    base_url = login[0] + "/v1/user/city/schedule"
    params = {'date': date}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if date == None:
        assert result['result'] == '4002'
    else:
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
