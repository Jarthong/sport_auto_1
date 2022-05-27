__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests
from interface.Feed_Comment_Controller.data_fixture import Feed_Comment_Controller


@pytest.mark.parametrize('rows',[10,20,50,100])
@pytest.mark.parametrize('userId',[None,Feed_Comment_Controller('user_id').result()[0]])
def test_v1_feed_feed(login,userId,rows):
    ''' 获取用户所有发表的微博动态功能接口'''
    base_url =login[0] + "/v1/feed/feed"
    params={'userId':userId,'page':1,'rows':rows}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    if userId is not None:
        total = Feed_Comment_Controller('count(*)',
                                        where="where user_id='{userId}' and  is_del=0".format(userId=userId)).result()[0]
        assert result['data']['total'] == total

    
if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
