__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests

from db_fixture.common import RandomVar, GlobalVar
from interface.Goods_Controller.data_fixture import  GoodsVar
# 资源类型：2,图片;3,视频
resType=[2,3]
#资源文件用途：1,用户相册图；2,IP推荐图；3,用户上传视频;4,直播直播封面;5,举报图片;6,直播回放封面;7,组织logo
purType=list(range(1,8))
rows =GoodsVar().rows
@pytest.mark.parametrize('resType',resType)
@pytest.mark.parametrize('purType',purType)
@pytest.mark.parametrize('rows',rows)

def test_v1_user__guest_albumFile(login,resType,purType,rows):
    ''' 查看相册文件列表'''
    base_url =login[0] + "/v1/user/_guest/albumFile"
    params={'userId': GlobalVar.GVar_hxm['user_id'], 'resType': resType, 'purType': purType, 'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    assert result['data']['total'] >=0
    if result['data']['total'] >0:
        assert result['data']['rows'] ==rows


    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
