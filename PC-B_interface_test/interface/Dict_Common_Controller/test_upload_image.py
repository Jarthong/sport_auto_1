import random

__author__ = 'huxm855'
import os
import requests

file = os.path.dirname(os.path.dirname(
    os.path.dirname((os.path.abspath(os.path.dirname(__file__)))))) + '\\common\\pictures\\' + str(
    random.choice(range(20))) + '.jpg'
files = {'file': open(file, 'rb')}


def test_upload_image(login):
    ''' 上传图片'''
    base_url = login.host + "/upload/image"
    r = requests.post(base_url, headers=login.headers, files=files, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data'] is not None


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
