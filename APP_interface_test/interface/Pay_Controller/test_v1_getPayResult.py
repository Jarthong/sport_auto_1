#!/user/bin/python
#encoding:utf-8

import pytest,os
from db_fixture.login_token import *
from interface.Pay_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
from db_fixture.getdata import *

class Test_GetPayResult(object):
    """获取支付结果"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/getPayResult"
        self.headers = login_match[-1]


    ordernumber = [Pay_Controller().Good_Order('seedp10'),Pay_Controller().Good_Order('seedp14100')]
    BUYER_USER_ID = ['seedp10','seedp14100']
    @pytest.mark.parametrize('orderNumber,BUYER_USER_ID',list(zip(ordernumber,BUYER_USER_ID)))
    def test_getpayresult(self,public,orderNumber,BUYER_USER_ID):
        """
        获取支付结果
        :param public:
        :return:
        """
        self.params = {
            "orderNumber":orderNumber,
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if BUYER_USER_ID == 'seedp10':
            assert self.result['msg'] == '成功'
        elif BUYER_USER_ID == 'seedp14100':
            assert '权限不足' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

















