__author__ = 'huxm855'

import os
import pytest
import requests

from db_fixture.getdata import GetData


@pytest.mark.parametrize('feedId', [GetData('feed_id',where='where digg_count>0').result(), None, 1111])
def test_v1_user_feed_digg(login,feedId):
    ''' 微博动态点赞功能接口'''
    base_url =login.host + "/v1/user/feed/digg"
    params={'feedId':feedId}
    print(params)
    r = requests.delete(base_url, headers=login.headers, params=params,verify=False)
    result = r.json()
    print(result)
    if feedId is not None:
        assert result['result'] in ('3022',0)
    else:
        assert result['msg'] == '参数错误[long@feedId]'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))


