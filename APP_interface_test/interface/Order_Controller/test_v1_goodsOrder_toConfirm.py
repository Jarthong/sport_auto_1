#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Order_Controller.data_fixture import Order_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_GoodsOrder_toConfirm(object):
    """去确认（商品）订单"""
    @pytest.fixture()
    def public(self,login_match):
        self.headers = login_match[-1]
        self.base_url = login_match[0] + "/v1/user/goodsOrder/toConfirm"

    skuCode = [Order_Controller().Goods_Sku_status(1),Order_Controller().Goods_Sku_status(2),
               Order_Controller().Goods_Sku_status(3),Order_Controller().Goods_Sku(4,1)]  #Order_Controller().Goods_Sku(4,1)
    status = [1,2,3,4]
    @pytest.mark.parametrize('skuCode,status',list(zip(skuCode,status)))
    def test_goodsorder_toconfirm(self,public,skuCode,status):
        """
        去确认（商品）订单
        :param public:
        :return:
        """
        self.params = {
            "detailList[0].skuCode":skuCode,
            "detailList[0].quantity":1
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if status == 1:
            assert self.result['result'] == '20034'
            assert self.result['msg'] == '该商品已经下架'
        elif status == 2:
            assert '该商品未审核通过' in self.result['msg']
        elif status == 3:
            assert '20056' in self.result['result']
        elif status == 4:
            assert '成功' in self.result['msg']



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))




