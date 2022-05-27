from interface.Goods_Controller.data_fixture import Goods_Cotroller, GoodsVar

__author__ = 'huxm855'
# -*- coding: utf-8 -*-

import os

import pytest
import requests


cateCode=GoodsVar.cateCode

page=[10,50,100]
@pytest.mark.parametrize('cateCode',cateCode)
@pytest.mark.parametrize('page',page)

def test_api_v1_guest_goodsList(login,cateCode,page):
    ''' 根据 商品code 获取商品列表'''
    base_url =login[0] + "/v1/guest/goodsList"
    params={'cateCode':cateCode,
            'page':page,
            'rows':1,
            }
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
