# -*- coding: utf-8 -*-
__author__ = 'huxm855'

import os

import pytest
import requests
from interface.Device_Info_Controller.data_fixture import Device_Info_Controller

targetAntToken = [Device_Info_Controller().user_token(), 'sfwefe', None]


@pytest.mark.parametrize('targetAntToken', targetAntToken)
def test_api_v1_user_antTokenOrUserId(login, targetAntToken):
    ''' 根据 创建点对点会话'''
    base_url = login[0] + "/v1/chat/pearToPearSession"
    params = {'targetAntToken': targetAntToken}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if targetAntToken == None:
        assert result['msg'] == '参数错误[String@targetAntToken]'
    else:
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
