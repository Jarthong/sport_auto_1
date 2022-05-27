# -*- coding: utf-8 -*-
__author__ = 'huxm855'

import os
import requests

def test_v1_guest_deviceInfo_upload(login):
    ''' 上报设备信息'''
    base_url =login[0] + "/v1/guest/deviceInfo/upload"
    params={'screenWidth': 12, 'screenHeight': 36, 'webGLVersion':'2.6', 'gpuVersion': '2.6'}

    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['result'] in('2','1025')
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
