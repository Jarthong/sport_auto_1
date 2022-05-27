#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Coupon_Controller.data_fixture import Coupon_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_CouponDetail(object):
    """优惠券详情"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/coupon/detail"
        self.headers = login_match[-1]

    codeId = [Coupon_Controller().coupon()[0],None]
    @pytest.mark.parametrize('codeId',codeId)
    def test_coupondetail(self,public,codeId):
        """
        优惠券详情
        :param public:
        :return:
        """
        self.params = {
            "codeId":codeId
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['codeId'] is not None:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['codeId'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))





