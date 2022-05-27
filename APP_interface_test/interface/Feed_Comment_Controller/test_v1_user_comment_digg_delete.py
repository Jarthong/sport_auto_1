from db_fixture.getdata import GetData

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests

commentId=[GetData('comment_id','feed_comment_digg','is_del=0').result(), GetData('max(comment_id)','feed_comment_digg','is_del=0').result()+1,None]
seq =range(0,3)
@pytest.mark.parametrize('commentId,seq', list(zip(commentId,seq)))
def test_v1_user_comment_digg(login,commentId,seq):
    ''' 微博评论内容点赞功能接口'''
    base_url =login[0] + "/v1/user/comment/digg"
    params={'commentId':commentId}
    r = requests.delete(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)

    if commentId is not None:
            assert result['result'] in ('3025','0')
    else:
            assert result['msg'] ==  '参数错误[Long@commentId]'
if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))


