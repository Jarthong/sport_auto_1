__author__ = 'huxm855'

import os
import random

import requests

file = os.path.dirname(
    os.path.dirname((os.path.abspath(os.path.dirname(__file__))))) + '\\common\\pictures\\' + str(
    random.choice(range(10))) + '.jpg'
files = {'file': open(file, 'rb')}


def test_v1_user_upload_image(login):
    ''' 上传图片'''
    base_url = login.host + "/v1/user/upload/images"
    r = requests.post(base_url, headers=login.headers, files=files, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert len(result['data'])>0


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
