from interface.Goods_Controller.data_fixture import Goods_Cotroller, GoodsVar

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests


cateCode=GoodsVar.cateCode
page=[10,50,100]
@pytest.mark.parametrize('cateCode',cateCode,ids=cateCode)

def test_api_v1_guest_goodsList(login,cateCode):
    ''' 根据 goodsCode 获取商品详情'''
    base_url =login[0] + "/v1/guest/goods"
    params={'goodsCode':Goods_Cotroller().goods(column='goods_code',parent_cate_code=cateCode),

            }
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    assert result['msg'] == '成功'
    assert result['data']['goodsCode']== params['goodsCode']

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
