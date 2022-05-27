#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Order_Controller.data_fixture import *
from interface.Community_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_GoodsOrderCancer(object):
    """取消（商品）订单,状态 1: 待支付，2: 已支付，3: 支付失败，4: 已完成，5: 已关闭，6: 退款中，7: 已退货，9：预下单成功，10：已取消"""

    skuCode = [Order_Controller().Goods_Sku(4, 1)]
    @pytest.mark.parametrize('skuCode',skuCode)
    def test_goodsOrdercancel(self,login_match,skuCode):
        """
        取消（商品）订单
        :param public:
        :return:
        """
        self.headers = login_match[-1]
        self.base_url = login_match[0] + "/v1/user/goodsOrder/cancel"
        self.second_url = login_match[0] + "/v1/user/goodsOrder/create"
        a = requests.post(self.second_url,headers = self.headers,verify=False,params={"detailList[0].skuCode":str(skuCode),
            "detailList[0].quantity":'1'})
        self.result2 = a.json()
        print(self.result2)
        b = self.result2['data']['orderNumber']
        self.params = {
            "orderNumber":b,
            "cancelReason":'autotest商品拍错了',
        }
        r = requests.delete(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


