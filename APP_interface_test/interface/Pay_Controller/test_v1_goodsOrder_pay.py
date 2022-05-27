#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Pay_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
from db_fixture.getdata import *

class Test_GoodsOrder_Pay(object):
    """获取支付结果"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/goodsOrder/pay"
        self.headers = login_match[-1]


    ordernumber = [Pay_Controller().Good_Order('seedp10')]
    @pytest.mark.parametrize('orderNumber',ordernumber)
    def test_goodsorder_pay(self,public,orderNumber):
        """
        获取支付结果
        :param public:
        :return:
        """
        self.params = {
            "orderNumber":orderNumber,
            "payType":'without.all.balance',
            "transPwd":Encrypt().md5Encode("905987")
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert '订单失效' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


















