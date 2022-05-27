#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Order_Controller.data_fixture import Order_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_GoodsOrderCreate(object):
    """创建（商品）订单"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/goodsOrder/create"
        self.headers = login_match[-1]

    skuCode = [Order_Controller().Goods_Sku(4,1),Order_Controller().Goods_Sku_null(1)]
    status = [4,1]
    @pytest.mark.parametrize('skuCode,status',list(zip(skuCode,status)))
    def test_GoodsOrdercreate(self,public,skuCode,status):
        """
        创建（商品）订单
        :param public:
        :return:
        """
        self.params = {
            "detailList[0].skuCode":skuCode,
            "detailList[0].quantity":'1'
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if status==4:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif status==1:
            assert self.result['msg'] == '抱歉，预热中的商品暂不能购买!'
            assert self.result['result'] == '20046'


    skuCode = [Order_Controller().Goods_Sku(4,2),Order_Controller().Goods_Sku_null(1)]
    status = [4,1]
    @pytest.mark.parametrize('skuCode,status',list(zip(skuCode,status)))
    def test_GoodsOrdercreate2(self,public,skuCode,status):
        """
        创建（商品）订单
        :param public:
        :return:
        """
        self.params = {
            "detailList[0].skuCode":skuCode,
            "detailList[0].quantity":'2'
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if status == 4:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif status==1:
            assert self.result['msg'] == '您够买的商品总数量超过限购数量'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))




