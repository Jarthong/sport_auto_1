#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Pay_Controller.data_fixture import Pay_Controller

urllib3.disable_warnings(InsecureRequestWarning)

class Test_toPay(object):
    """去支付"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/toPay"
        self.headers = login_match[-1]


    ordernumber = [Pay_Controller().Good_Order('seedp10')]
    @pytest.mark.parametrize('orderNumber',ordernumber)
    def test_topay(self,public,orderNumber):
        """
        去支付
        :param public:
        :return:
        """
        self.params = {
            "orderNumber":orderNumber
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert '订单失效' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



















