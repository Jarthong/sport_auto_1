__author__ = 'huxm855'
import os

import requests


def test_preview_goods(login):
    ''' 预览商品数据'''
    base_url =login.host + "/preview/goods"
    params={'rdmkey':12}
    r = requests.get(base_url, headers=login.headers, params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  'redisKey不存在'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))