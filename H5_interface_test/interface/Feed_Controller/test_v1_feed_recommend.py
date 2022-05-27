__author__ = 'huxm855'
import os

import pytest
import requests

from db_fixture.getdata import GetData


@pytest.mark.parametrize('rows', [10, 20, 50, 100])
def test_v1_feed_recommend(login, rows):
    ''' 获取微博推荐的动态功能接口'''
    base_url = login.host + "/v1/feed/recommend"
    params = {'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    total = GetData('count(*)', where="where is_recommend=1 and  is_del=0").result()
    assert result['msg'] == '成功'
    assert result['data']['total'] == total



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
