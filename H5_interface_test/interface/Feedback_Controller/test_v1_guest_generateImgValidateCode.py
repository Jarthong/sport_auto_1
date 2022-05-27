__author__ = 'huxm855'

import os
import pytest
import requests


@pytest.mark.parametrize('type', range(1,7))

def test_v1_guest_generateImgValidateCode(login,type):
    ''' 生成图片验证码'''
    base_url =login.host + "/v1/guest/generateImgValidateCode"
    params = {'width': 12, 'height': 55, 'type': type}
    r = requests.get(base_url, headers=login.headers, params=params,verify=False)
    result = r.json()
    print(result)
    assert result['result']==  '0'
    assert result['data']['image'] is not None
    assert result['data']['key'] is not None



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))