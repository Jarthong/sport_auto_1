__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests

from db_fixture.common import GlobalVar
import os

import pytest
import requests
from db_fixture.common import GlobalVar

userId = [GlobalVar.GVar_hxm['user_id'], 'sfwefe', None]


@pytest.mark.parametrize('userId', userId)
def test_api_v1_user_antTokenOrUserId(login, userId):
    ''' 获取antToken和userId '''
    base_url = login[0] + "/v1/user/antTokenOrUserId"
    params = {'userId': userId}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    if userId == None:
        assert result['msg'] == '对照接口文档,检查接口必输参数是否有值或参数类型是否正确...'
    else:
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
