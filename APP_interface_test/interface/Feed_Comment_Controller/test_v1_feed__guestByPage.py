__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests


@pytest.mark.parametrize('rows',[10,20,50,100])
def test_v1_feed__guestByPage(login,rows):
    ''' 未登录时首页展示所有微博动态功能接口(带分页)'''
    base_url =login[0] + "/v1/feed/_guestByPage"
    params={'page':1,'rows':rows}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    assert result['data']['endRow']==rows
if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
