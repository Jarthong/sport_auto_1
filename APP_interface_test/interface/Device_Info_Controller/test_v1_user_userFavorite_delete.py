__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests
from interface.Device_Info_Controller.data_fixture import Device_Info_Controller

bizId, favoriteType = Device_Info_Controller().user_favorite(column='biz_id,favorite_type')
@pytest.mark.skipif(favoriteType==0,reason='无用户收藏数据，可删除')
def test_v1_user_userFavorite(login):
    ''' 删除用户收藏'''
    base_url =login[0] + "/v1/user/userFavorite"
    params={'bizId':bizId,'favoriteType':favoriteType}
    r = requests.delete(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    assert result['result']==  '0'
    assert result['msg']==  '成功'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
