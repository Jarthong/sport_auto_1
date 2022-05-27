__author__ = 'huxm855'

import os
import requests


def test_v1_file_imageUrl(login):
    ''' 获取图片'''
    base_url =login[0] + "/v1/file/imageUrl"
    params = {'filePath': '/f/20180202/sport/feed/i/c75baea408db4294a28d7d965656e50d.jpg','width':100,'height':100}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    assert result['data']['resUrl']==  'https://file.hhlysport.com/f/20180202/sport/feed/i/c75baea408db4294a28d7d965656e50d_100x100.jpg'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))