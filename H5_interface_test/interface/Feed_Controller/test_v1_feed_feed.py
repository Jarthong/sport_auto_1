__author__ = 'huxm855'
import os
import pytest
import requests

from db_fixture.getdata import GetData


@pytest.mark.parametrize('rows',[10,20,50,100])
@pytest.mark.parametrize('userId',[None,GetData('user_id').result()[0]])
def test_v1_feed_feed(login,userId,rows):
    ''' 获取用户所有发表的微博动态功能接口'''
    base_url =login.host + "/v1/feed/feed"
    params={'userId':userId,'page':1,'rows':rows}
    r = requests.get(base_url, headers=login.headers, params=params,verify=False)
    result = r.json()
    print(result)
    if userId is not None:
        total = GetData('count(*)',
                                        where="where user_id='{userId}' and  is_del=0".format(userId=userId)).result()
        assert result['msg']==  '成功'
        assert result['data']['total'] == total
    else:
        assert result['msg']== '参数错误[String@userId]'




if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))