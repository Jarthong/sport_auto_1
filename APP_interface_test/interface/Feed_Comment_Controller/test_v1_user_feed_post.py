__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
@pytest.mark.parametrize('title', ['autotest_title',None])
@pytest.mark.parametrize('content', ['autotest_content',None])
def test_v1_user_feed(login,title,content):
    ''' 发送微博动态功能接口'''
    base_url =login[0] + "/v1/user/feed"
    params={'title':title,'feedContents[0].content':content,'feedContents[0].contentType':1}
    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if title !=None and content!=None:

        assert result['msg']==  '成功'
    elif title==None:
        assert result['msg']==   '[{"name":"title","message":"微博动态标题不能为空"}]'

    elif content==None:
        assert result['msg']==  '接口异常（通用错误）'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
