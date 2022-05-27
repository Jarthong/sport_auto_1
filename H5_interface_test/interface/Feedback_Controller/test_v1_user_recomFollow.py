__author__ = 'huxm855'

import os
import requests


def test_v1_user_recomFollow(login):
    ''' 推荐关注,随机取前十条'''
    base_url =login.host + "/v1/user/recomFollow"
    r = requests.get(base_url, headers=login.headers, verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))