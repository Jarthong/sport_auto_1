from db_fixture.common import GlobalVar

__author__ = 'huxm855'

import os

import pytest
import requests
# 轮播图位置：
# 6001, 首页->资讯;
# 6002, 视频->节目点播;
# 6003, 视频->个人秀;
# 6004, 首页->banner图
from db_fixture.login_token import login_token
from db_fixture.getdata import *


@pytest.fixture(params=range(1, 5))
def login(request):
    host, userId, headers = login_token(phone=GlobalVar.GVar_hxm['user_phone'],password=GlobalVar.GVar_hxm['passworld'],ClientType=request.param).userInfo()

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)

    return host, userId, request.param, headers


@pytest.mark.parametrize('resPosition', range(6001, 6005))
@pytest.mark.parametrize('rows', [10, 20, 50, 100])
def test_v1_file_playturn(login, resPosition, rows):
    ''' 获取轮播资源'''
    base_url = login[0] + "/v1/file/playturn"
    device_type = login[-2]
    count_resPosition = GetData('count(res_Position)', table='app_play_turn',
                                where=" STATUS=1 and res_Position={res_Position} and device_type={device_type} GROUP BY res_Position".format(
                                    res_Position=resPosition, device_type=device_type)).result()

    params = {'resPosition': resPosition, 'rows': rows}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    if count_resPosition == None:
        assert result['data']['total'] == 0
    else:
        assert result['data']['total'] == count_resPosition


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
