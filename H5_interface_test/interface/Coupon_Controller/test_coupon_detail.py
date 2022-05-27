#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *

code_id = [GetData(column='CODE_ID',table='coupon',where="where USER_ID = 'seedp10'").result()]
@pytest.mark.parametrize('code_id',code_id)
def test_coupon_detail(login_hq3,code_id):
    """
    优惠券详情
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/coupon/couponDetail"
    params = {
        'code_id':code_id
    }
    print(params['code_id'])
    r = requests.get(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






