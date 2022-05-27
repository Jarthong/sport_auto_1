#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *

coupon_num = [GetData(column='count(*)',table='coupon',where="where USER_ID='seedp10'").result()]

def test_coupon(login_hq3):
    """
    可用优惠券列表
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/coupon/coupon"
    params = {
        'page':1,
        'rows':15
    }
    r = requests.get(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    assert result['data']['total'] in coupon_num
    assert result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






