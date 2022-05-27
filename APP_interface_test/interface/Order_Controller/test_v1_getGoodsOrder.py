#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Order_Controller.data_fixture import Order_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_getGoodsOrder(object):
    """获取订单"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/getGoodsOrder"
        self.headers = login_match[-1]

    orderNumber = [Order_Controller().Good_Order(GlobalVar().ORG_USERIDS[0],4),
                   Order_Controller().Good_Order(GlobalVar().ORG_USERIDS[0],5),None,25086160564125696]  # 状态 1: 待支付，2: 已支付，3: 支付失败，4: 已完成，5: 已关闭，6: 退款中，7: 已退货，9：预下单成功，10：已取消
    @pytest.mark.parametrize('orderNumber',orderNumber)
    def test_getGoodsOrder(self,public,orderNumber):
        """
        获取订单
        :param public:
        :return:
        """
        self.params = {
            "orderNumber":orderNumber
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['orderNumber'] is not None and self.params['orderNumber'] != 25086160564125696:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['orderNumber'] is None:
            assert self.result['result'] == '4002'
            assert '参数错误' in self.result['msg']
        elif self.params['orderNumber'] == '25086160564125696':
            assert self.result['result'] == '1009'
            assert self.result['msg'] == '用户权限不足'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



