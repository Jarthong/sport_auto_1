#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.getdata import *


batchId = [GetData(column='a.BATCH_ID',table='coupon_code a LEFT JOIN coupon b ON a.BATCH_ID = b.BATCH_ID',where="where b.USER_ID = 'seedp10' AND a.CODE_STATUS = 2").result(),None]
@pytest.mark.parametrize('batchId',batchId)
def test_coupon_post(login_hq3,batchId):
    """
    领取优惠券
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/coupon/coupon"
    params = {
        'batchId':batchId
    }
    r = requests.post(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if batchId == None:
        assert '参数错误' in result['msg']
    else:
        assert '已经领取过优惠券' in result['msg']
        assert result['result'] == '16017'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






