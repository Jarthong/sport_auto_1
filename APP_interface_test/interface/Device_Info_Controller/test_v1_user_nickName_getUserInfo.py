__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests
from db_fixture.common import GlobalVar
from interface.Device_Info_Controller.data_fixture import Device_Info_Controller


@pytest.mark.parametrize('nickName', [Device_Info_Controller().user_info(column='nick_name')[0], None])
def test_v1_user_nickName_getUserInfo(login, nickName):
    ''' 根据用户昵称获取用户信息'''
    base_url = login[0] + "/v1/user/nickName/getUserInfo"
    params = {'nickName': nickName}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if nickName is None:
        assert result['result'] == '4002'
    else:
        assert result['msg'] == '成功'
        assert result['data']['userId'] == GlobalVar.GVar_hxm['user_id']
        assert result['data']['nickName'] in nickName


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
