#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Coupon_Controller.data_fixture import Coupon_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_CouponReceive(object):
    """领取优惠券"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/coupon/receive"
        self.headers = login_match[-1]

    batchId = [Coupon_Controller().coupon_code(2)[0],None]
    @pytest.mark.parametrize('batchId',batchId)
    def test_couponreceive(self,public,batchId):
        """
        领取优惠券
        :param public:
        :return:
        """
        self.params = {
            "batchId":batchId
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['batchId'] is not None:
            assert self.result['msg'] == '已经领取过优惠券'
        elif self.params['batchId'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))







