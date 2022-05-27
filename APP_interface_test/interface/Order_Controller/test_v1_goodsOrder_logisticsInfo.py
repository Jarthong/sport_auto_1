#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Order_Controller.data_fixture import Order_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_GoodsOrder_LogisticsInfo(object):
    """获取物流信息"""
    @pytest.fixture()
    def public(self,login_match):
        self.headers = login_match[-1]
        self.base_url = login_match[0] + "/v1/user/goodsOrder/logisticsInfo"

    orderNumber = [Order_Controller().Good_Order('seedp10',4),Order_Controller().Good_Order('seedp543575',4)]
    userid = ['seedp10','seedp543575']
    @pytest.mark.parametrize('orderNumber,userid',list(zip(orderNumber,userid)))
    def test_goodsorder_logisticsinfo(self,public,orderNumber,userid):
        """
        获取物流信息
        :param public:
        :return:
        """
        self.params = {
            "orderNumber":orderNumber
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if userid == 'seedp10':
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif userid == 'seedp543575':
            assert '用户权限不足' in self.result['msg']



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



