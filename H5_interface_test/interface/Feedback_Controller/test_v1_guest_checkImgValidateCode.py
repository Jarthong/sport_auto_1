__author__ = 'huxm855'

import os

import pytest
import requests


@pytest.mark.parametrize('type', range(1, 3))
def test_v1_guest_checkImgValidateCode(login, type):
    ''' 校验图片验证码'''
    base_url = login.host + "/v1/guest/checkImgValidateCode"
    params = {'randomKey': 1232, 'imgValidateCode': 666666, 'type': type}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
