__author__ = 'huxm855'

import os

import requests


def test_v1_user_removeUserContactPerson(login):
    ''' 删除用户联系人'''
    base_url = login.host + "/v1/user/removeUserContactPerson"
    params = {'ids': [1,2]}
    r = requests.delete(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
