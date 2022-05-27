__author__ = 'huxm855'
import os
import pytest
import requests

from db_fixture.getdata import GetData


@pytest.mark.parametrize('rows',[10,20,50,100])
@pytest.mark.parametrize('feedId',[GetData('feed_id',table='feed_comment').result(),None,1111])
def test_v1_feed_comment(login,feedId,rows):
    ''' 获取微博所有评论详情信息功能接口'''
    base_url =login.host + "/v1/feed/comment"
    params={'feedId':feedId,'page':1,'rows':rows}
    r = requests.get(base_url, headers=login.headers, params=params,verify=False)
    result = r.json()
    print(result)
    if feedId is not None:
        total = GetData('count(*)', table='feed_comment',
                                        where='where feed_id={feed_id} and  is_del=0'.format(feed_id=feedId)).result()
        assert result['msg'] == '成功'
        assert result['data']['total'] == total
    else:
        assert result['msg'] == '参数错误[long@feedId]'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))