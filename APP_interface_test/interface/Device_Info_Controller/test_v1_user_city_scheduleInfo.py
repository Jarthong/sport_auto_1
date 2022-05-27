__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests


@pytest.mark.parametrize('eventDate', [None, '2018-1-1'])
def test_v1_user_city_scheduleInfo(login, eventDate):
    ''' 查询用户的日程详情信息列表接口'''
    base_url = login[0] + "/v1/user/city/scheduleInfo"
    params = {'eventDate': eventDate}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if eventDate == None:
        assert result['result'] == '4002'
    else:
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
