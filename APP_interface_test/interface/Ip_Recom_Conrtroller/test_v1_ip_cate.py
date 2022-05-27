__author__ = 'huxm855'
import os

import pytest
import requests


@pytest.mark.parametrize('cateId', range(1, 10))
def test_v1_ip_cate(login, cateId):
    ''' 获取更多个人主页模块显示功能接口'''
    base_url = login[0] + "/v1/ip/cate"
    params = {'cateId': cateId, 'page': 1, 'rows': 10}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
