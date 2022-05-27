#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Coupon_Controller.data_fixture import Coupon_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_CouponExchange(object):
    """兑换优惠券"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/coupon/exchange"
        self.headers = login_match[-1]


    # exchangeCode = [Coupon_Controller().coupon_code(1)[1],Coupon_Controller().coupon_code(2)[1],
    #                 Coupon_Controller().coupon_code_not(4,4),Coupon_Controller().coupon_code_not(5,5)]
    code_status = [2,4,5]
    exchangeCode = [Coupon_Controller().coupon_code(2)[1],Coupon_Controller().coupon_code(4)[1],Coupon_Controller().coupon_code(5)[1]]
    @pytest.mark.parametrize('exchangeCode,code_status',list(zip(exchangeCode,code_status)))
    def test_couponexchange(self,public,exchangeCode,code_status):
        """
        兑换优惠券
        CODE_STATUS:1,未使用,2已使用,3使用中(未用完),4已过期,5已作废
        :param public:
        :return:
        """
        self.params = {
            "exchangeCode":exchangeCode
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if code_status == 2:
            assert self.result['msg'] == '兑换码已使用'
            assert self.result['result'] == '16028'
        elif code_status == 4:
            assert self.result['msg'] == '已经领取过优惠券'
        elif code_status == 5:
            assert self.result['msg'] == '已经领取过优惠券'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))





