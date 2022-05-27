__author__ = 'huxm855'

import os
import requests


def test_v1_file_videoResource(login):
    ''' 获取资源视频内容功能接口'''
    base_url = login[0] + "/v1/file/videoResource"
    params = {'filePath': '/f/20180202/sport/feed/v/31dd56255a134ee3a455a693c30e8255.mp4', 'width': 100, 'second': 1}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    assert  len(r.content)==1668
    assert  r.status_code==200


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
