__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
# 该接口在哪操作出现，0，-2 响应失败 IP_CATE_ID：254
# 用户类型 0：全部 ，-1：认证用户， -2：未认证用户，其他类型传ipCateId
from interface.Device_Info_Controller.data_fixture import GoodsVar


@pytest.mark.parametrize('ipCateId', [0, -1, -2, 254, None])
@pytest.mark.parametrize('pageSize', GoodsVar().rows)
def test_v1_user_listUserByIp(login, ipCateId, pageSize):
    ''' 用户列表'''
    base_url = login[0] + "/v1/user/listUserByIp"
    params = {'ipCateId': ipCateId, 'pageNO': 1, 'pageSize': pageSize}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
