__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import requests
from interface.Device_Info_Controller.data_fixture import Device_Info_Controller


def test_v1_user_myInfo(login):
    ''' 获取我的信息'''
    base_url =login[0] + "/v1/user/myInfo"
    r = requests.get(base_url, headers=login[-1],verify=False)
    result = r.json()
    userId,nickName,sex,authType=Device_Info_Controller().user_info(column=' user_id,nick_name,sex,auth_type')[0]
    print(result)
    assert result['msg']==  '成功'
    assert result['data']['userId']==userId
    assert result['data']['nickName']==nickName
    assert result['data']['sex']==sex
    assert result['data']['authType']==authType



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
