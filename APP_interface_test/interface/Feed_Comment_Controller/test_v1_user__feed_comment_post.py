from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import random

import pytest
import requests



@pytest.mark.parametrize('feedId', [GetData('feed_id',where='is_del=0').result(), None, 1111])
@pytest.mark.parametrize('content', [None, 'autoTest'*10])
@pytest.mark.parametrize('fileUrl', [None, random.choice(GlobalVar.IMGS)])
def test_v1_user__feed_comment(login, feedId,content,fileUrl):
    ''' 微博评论功能接口'''
    base_url = login[0] + "/v1/user/_feed/comment"
    params = {'feedId': feedId,'content':content,'fileUrl':fileUrl}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if feedId ==None:
        assert result['msg'] == '[{"name":"feedId","message":"微博帖子Id不能为空"}]'

    elif feedId== 1111:
        assert result['msg'] == '贴子不存在'
    else:
            assert result['msg'] in ('成功','评论内容和图片不能同时为空')



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
