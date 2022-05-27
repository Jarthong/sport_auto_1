from db_fixture.common import GlobalVar
from interface.Device_Info_Controller.data_fixture import GoodsVar
from interface.Goods_Controller.data_fixture import Goods_Cotroller

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests



userId = [GlobalVar.GVar_hxm['user_id'], 'sfwefe', None]

cateCode=GoodsVar().cateCode
@pytest.mark.parametrize('cateCode',cateCode)
def test_api_v1_group_goods_goodsTemplateInfo(login,cateCode):
    ''' 根据 商品code 获取商品列表'''
    base_url = login[0] + "/v1/group/goods/goodsTemplateInfo"
    goodsCode,goodsCateCode1,goodsCateCode,orderNumber,skuCode=Goods_Cotroller().goods_order(cateCode=cateCode)
    params = {'goodsCode':goodsCode,
                'goodsCateCode1':goodsCateCode1,
                'goodsCateCode':goodsCateCode,
                'orderNumber':orderNumber,
                'skuCode':skuCode,
                }

    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)

    assert  result['result']=='0'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
