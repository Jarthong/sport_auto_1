__author__ = 'huxm855'
import os

import pytest
import requests

from db_fixture.getdata import *
from interface.Goods_Controller.data_fixture import *

cateCode = GoodsVar.cateCode


@pytest.mark.parametrize('langType', ['zh_CN', 'en', None])
def test_v1_system_params(login, langType):
    ''' 设置系统参数'''
    base_url = login[0] + "/v1/system/params"
    params = {'langType': langType}
    r = requests.put(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if langType != None:
        assert result['msg'] == '成功'
        assert result['data']['langType'] == langType.lower()
    else:
        assert result['result'] == '4002'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
