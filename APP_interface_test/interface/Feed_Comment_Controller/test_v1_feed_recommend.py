__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests

from interface.Feed_Comment_Controller.data_fixture import Feed_Comment_Controller


@pytest.mark.parametrize('rows', [10, 20, 50, 100])
def test_v1_feed_recommend(login, rows):
    ''' 获取微博推荐的动态功能接口'''
    base_url = login[0] + "/v1/feed/recommend"
    params = {'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    total = Feed_Comment_Controller('count(*)', where="where is_recommend=1 and  is_del=0").result()[0]
    assert result['msg'] == '成功'
    assert result['data']['total'] == total



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
