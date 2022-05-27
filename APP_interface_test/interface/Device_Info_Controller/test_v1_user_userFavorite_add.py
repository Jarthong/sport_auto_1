__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests

from interface.Goods_Controller.data_fixture import GoodsVar, Goods_Cotroller

''' 添加用户收藏-FAVORITE_TYPE	收藏类型(1资讯，2视频,3商品)'''

goodsType=GoodsVar.cateCode
@pytest.mark.parametrize('goodsType',goodsType)

def test_v1_user_userFavorite_post(login,goodsType):
    ''' 添加用户收藏-3商品'''
    base_url =login[0] + "/v1/user/userFavorite"
    params={'bizId':Goods_Cotroller().goods(column='goods_code',parent_cate_code=goodsType),'favoriteType':3}
    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    assert result== {'result': '0', 'msg': '成功'}

if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
