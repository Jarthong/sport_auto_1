__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import requests


def test_v1_user_recomFollow(login,):
    ''' 推荐关注,随机取前十条'''
    base_url =login[0] + "/v1/user/recomFollow"
    r = requests.get(base_url, headers=login[-1], verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
