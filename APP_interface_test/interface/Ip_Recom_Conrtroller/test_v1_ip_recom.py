__author__ = 'huxm855'

import os

import pytest
import requests

from db_fixture.getdata import GetData


@pytest.mark.parametrize('rows',[10,20,50,100])

def test_v1_ip_recom(login,rows):
    ''' 获取推荐Ip列表'''
    base_url =login[0] + "/v1/ip/recom"
    params = { 'page': 1, 'rows': rows}
    total = GetData('count(*)', table='app_ip_recom', where=" `STATUS`=1").result()
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    assert result['data']['total']== total


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))