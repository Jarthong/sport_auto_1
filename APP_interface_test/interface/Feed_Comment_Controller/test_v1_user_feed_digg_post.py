from db_fixture.getdata import GetData

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests

@pytest.mark.parametrize('feedId', [GetData('feed_id',where=' is_del=0').result(), None, 1111])
def test_v1_user_feed_digg(login,feedId):
    ''' 微博动态点赞功能接口'''
    base_url =login[0] + "/v1/user/feed/digg"
    params={'feedId':feedId}
    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if feedId in(None,1111):
        assert result['result'] in ('1000','4002','2')
    else:
        assert result['msg']  in ['该帖子已经被点赞，请稍后再试！','成功']

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))


