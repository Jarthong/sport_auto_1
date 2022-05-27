from interface.Goods_Controller.data_fixture import Goods_Cotroller

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import re
import requests

#在系统中不存在
#sku在系统中存在第一次加入购物车：根据限购数量测试:限购数量为0，随机添加小于库存数量的值，大于库存数量的值，等于库存值，限购数量大于0，添加等于限购数量，小于限购数量，大于限购数量的值

@pytest.mark.parametrize('skuCode,num',[('asfsffsfwe',1),

Goods_Cotroller().goods_sku(column='sku_code,1'),
Goods_Cotroller().goods_sku(column='sku_code,1',parent_cate_code='V12'),
Goods_Cotroller().goods_sku(column='sku_code,1',parent_cate_code='V18')
                                        ])
def test_api_v1_shopping_add(login,skuCode,num):
    ''' 根据 userid  添加商品到购物车'''
    base_url =login[0] + "/v1/shopping/add"
    params= {'detailList[0].skuCode':skuCode,
             'detailList[0].num':num
             }
    r = requests.post(base_url, headers=login[-1],params=params,verify=False)
    result = r.json()
    print(result)
    if skuCode=='asfsffsfwe':
        assert result['msg'] == '商品在数据库中不存在！'
    else:
        assert re.search('SKU状态不能购买|抱歉，商品对应的赛事已报名截止不能购买|成功|该商品您购买数量超过限购的数量|该商品不允许组织用户购买|该商品只能个人帐号购买|培训商品每次只能购买一个',result['msg'])

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
