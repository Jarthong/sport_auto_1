__author__ = 'huxm855'

import os
import pytest
import requests

from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

commentId=[GetData('comment_id','feed_comment_digg','where is_del=0  and user_id=\'{userId}\''.format(userId=GlobalVar.GVar['user_id'])).result(),None]
@pytest.mark.parametrize('commentId', commentId)
def test_v1_user_comment_digg(login,commentId):
    ''' 微博评论内容点赞功能接口'''
    base_url =login.host + "/v1/user/comment/digg"
    params={'commentId':commentId}
    r = requests.delete(base_url, headers=login.headers, params=params,verify=False)
    result = r.json()
    print(params)
    print(result)

    if commentId is not None:
            assert result['result'] =='0'
            assert result['msg'] =='成功'
    else:
            assert result['msg'] ==  '参数错误[Long@commentId]'
if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))


