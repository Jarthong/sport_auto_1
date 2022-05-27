import os
import random

import requests

__author__ = 'huxm855'

# 上传文件
pictures = os.path.dirname(
    os.path.dirname((os.path.abspath(os.path.dirname(__file__))))) + '\\common\\pictures\\' + str(
    random.choice(range(20))) + '.jpg'


def test_upload_file(login):
    ''' 上传文件'''
    base_url = login.host + "/upload/file"
    files = {'file': open(pictures, 'rb')}
    r = requests.post(base_url, headers=login.headers, files=files, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data'] is not None


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
