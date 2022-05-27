from db_fixture.getdata import GetData

__author__ = 'huxm855'

import os

import pytest
import requests



@pytest.mark.parametrize('feedId', [GetData('feed_id',where='is_del=0').result(), None])
def test_v1_feed(login, feedId):
    ''' 获取单条微博动态详情信息功能接口'''
    base_url = login[0] + "/v1/feed"
    params = {'feedId': feedId}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if feedId is not None:
        assert result['msg'] == '成功'
    else:
        assert result['msg'] == '参数错误[long@feedId]'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
