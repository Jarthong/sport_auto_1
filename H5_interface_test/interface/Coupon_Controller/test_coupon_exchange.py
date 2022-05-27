#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *
from db_fixture.common import *


code_2 = [GetData('a.exchange_code','coupon_code a,coupon b',"where a.BATCH_ID = b.BATCH_ID and b.USER_ID = '{USER_ID}' and a.CODE_STATUS = {CODE_STATUS}".format(USER_ID=GlobalVar.GVar_hq['user_id3'],CODE_STATUS=2)).result()]
code_4 = [GetData('a.exchange_code','coupon_code a,coupon b',"where a.BATCH_ID = b.BATCH_ID and b.USER_ID = '{USER_ID}' and a.CODE_STATUS = {CODE_STATUS}".format(USER_ID=GlobalVar.GVar_hq['user_id3'],CODE_STATUS=4)).result()]
code_5 = [GetData('a.exchange_code','coupon_code a,coupon b',"where a.BATCH_ID = b.BATCH_ID and b.USER_ID = '{USER_ID}' and a.CODE_STATUS = {CODE_STATUS}".format(USER_ID=GlobalVar.GVar_hq['user_id3'],CODE_STATUS=5)).result()]
exchangeCode = [code_2,code_4,code_5]
@pytest.mark.parametrize('exchangeCode',exchangeCode)
def test_coupon_exchange(login_hq3,exchangeCode):
    """
    兑换优惠券
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/coupon/exchange"
    params = {
        'exchangeCode':exchangeCode
    }
    r = requests.post(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if params['exchangeCode'] == code_2:
        assert result['msg'] == '兑换码已使用' and result['result'] == '16028'
    elif params['exchangeCode'] == code_4:
        assert result['msg'] == '已经领取过优惠券' and result['result'] == '16017'
    elif params['exchangeCode'] == code_5:
        assert result['msg'] == '已经领取过优惠券' and result['result'] == '16017'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






