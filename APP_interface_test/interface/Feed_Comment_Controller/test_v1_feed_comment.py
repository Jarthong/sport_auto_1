__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests
from interface.Feed_Comment_Controller.data_fixture import Feed_Comment_Controller


@pytest.mark.parametrize('rows',[10,20,50,100])
@pytest.mark.parametrize('feedId',[Feed_Comment_Controller('feed_id',table='feed_comment').result()[0],None,1111])
def test_v1_feed_comment(login,feedId,rows):
    ''' 获取微博所有评论详情信息功能接口'''
    base_url =login[0] + "/v1/feed/comment"
    params={'feedId':feedId,'page':1,'rows':rows}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if feedId is not None:
        total = Feed_Comment_Controller('count(*)', table='feed_comment',
                                        where='where feed_id={feed_id} and  is_del=0'.format(feed_id=feedId)).result()[0]
        assert result['msg'] == '成功'
        assert result['data']['total'] == total
    else:
        assert result['msg'] == '参数错误[long@feedId]'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
