__author__ = 'huxm855'

import os
import requests


def test_v1_file_imageCover(login):
    ''' 获取资源图片缩略图功能接口'''
    base_url = login[0] + "/v1/file/imageCover"
    params = {'filePath': '/f/20180202/sport/feed/i/c75baea408db4294a28d7d965656e50d.jpg', 'width': 100}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    assert len(r.content) > 2000
    assert r.status_code == 200


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
