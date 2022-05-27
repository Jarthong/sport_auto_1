__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests
from interface.Feed_Comment_Controller.data_fixture import Feed_Comment_Controller

#帖子内容
@pytest.mark.parametrize('feedId',[Feed_Comment_Controller('feed_id',table='feed_content').result(),None,1111])
@pytest.mark.parametrize('contentType',range(1,4))
def test_v1_feed_feedContent(login,feedId,contentType):
    ''' 查看微博动态内容信息功能接口'''
    base_url =login[0] + "/v1/feed/feedContent"
    params={'feedId':feedId,'contentType':contentType}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if feedId is not None:
        assert result['msg'] == '成功'
    else:
        assert result['msg'] == '参数错误[long@feedId]'
if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
