from db_fixture.common import GlobalVar

__author__ = 'huxm855'

import os
import pytest
import requests

from db_fixture.getdata import GetData


@pytest.mark.parametrize('feedId', [GetData('feed_id').result(), None, 1111])
def test_v1_user_feed_digg(login,feedId):
    ''' 微博动态点赞功能接口'''
    base_url =login.host + "/v1/user/feed/digg"
    params={'feedId':feedId,'userId':GlobalVar.GVar['user_id']}
    r = requests.post(base_url, headers=login.headers, params=params,verify=False)
    result = r.json()
    print(result)
    if feedId in(None,1111):
        assert result['result'] in ('4002','2','1000')
    else:
        assert result['msg'] in ('该帖子已经被点赞，请稍后再试！','成功')

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))


