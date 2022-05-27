#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests

totalAmount = [100,None]
@pytest.mark.parametrize('totalAmount',totalAmount)
def test_availableCoupon(login_hq3,totalAmount):
    """
    可用优惠券列表
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/coupon/availableCoupon"
    params = {
        'totalAmount':totalAmount,
        'page':1,
        'rows':15
    }
    r = requests.get(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if params['totalAmount'] == None:
        assert '参数错误' in result['msg']
    else:
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))





