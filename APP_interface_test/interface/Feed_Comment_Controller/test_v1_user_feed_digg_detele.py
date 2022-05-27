from db_fixture.getdata import GetData

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests
@pytest.mark.parametrize('feedId', [GetData('feed_id',where='digg_count>0 and is_del=0').result(), None, 1111])
def test_v1_user_feed_digg(login,feedId):
    ''' 微博动态点赞功能接口'''
    base_url =login[0] + "/v1/user/feed/digg"
    params={'feedId':feedId}
    r = requests.delete(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if feedId is not None:
        assert result['result'] in ('3022','0')
    else:
        assert result['msg'] == '参数错误[long@feedId]'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))


