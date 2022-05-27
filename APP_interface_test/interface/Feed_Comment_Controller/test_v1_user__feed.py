__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests


@pytest.mark.parametrize('rows', [10, 20, 50, 100])
def test_v1_user__feed(login, rows):
    ''' 登录时首页展示所有微博动态功能接口'''
    base_url = login[0] + "/v1/user/_feed"
    params = {'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data']['pageResultVO']['total'] >= 0


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
