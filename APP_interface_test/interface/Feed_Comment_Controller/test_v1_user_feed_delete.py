__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from interface.Feed_Comment_Controller.data_fixture import Feed_Comment_Controller


@pytest.mark.parametrize('feedId', [Feed_Comment_Controller('feed_id').result(), None, 1111])

def test_v1_user_feed(login,feedId):
    ''' 发送微博动态功能接口'''
    base_url =login[0] + "/v1/user/feed"
    params={'feedId':feedId}
    r = requests.delete(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if feedId is None:
        assert result['msg']== '参数错误[long@feedId]'
    elif feedId == 1111:
        assert result['msg'] in ( '该帖子已删除','成功')



    
if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
