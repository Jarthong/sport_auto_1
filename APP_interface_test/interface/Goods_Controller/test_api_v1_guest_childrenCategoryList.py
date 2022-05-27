from interface.Goods_Controller.data_fixture import GoodsVar, Goods_Cotroller

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import re
import requests


cateCode=GoodsVar.cateCode
@pytest.mark.parametrize('cateCode',cateCode,ids=cateCode)

def test_api_v1_guest_childrenCategoryList(login,cateCode):
    ''' 根据 商品code 获取下级分类列表'''
    base_url =login[0] + "/v1/guest/childrenCategoryList"
    params={'cateCode':cateCode}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()

    assert result['msg']==  '成功'
    if Goods_Cotroller().goods_category(parent_cate_code=cateCode):
        for cateCode in Goods_Cotroller().goods_category(parent_cate_code=cateCode):
            assert re.search(cateCode,str( result['data']))


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
