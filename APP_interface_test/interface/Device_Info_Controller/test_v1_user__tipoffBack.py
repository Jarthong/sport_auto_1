__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
# 举报原因类型
from db_fixture.common import RandomVar


@pytest.mark.parametrize('causeCate', list(range(4001, 4006)))
# 反馈文本
@pytest.mark.parametrize('cause', ['autotest' + RandomVar.random_char_upper(5)])
# 举报类型
@pytest.mark.parametrize('tipoffType,resId',
                         list(zip(list(range(1, 8)), [14144, 67268, 1073, 'seedp298', 34288, 10284, 199083])))
def test_v1_user__tipoffBack(login, cause, causeCate, tipoffType, resId):
    ''' 举报'''
    base_url = login[0] + "/v1/user/_tipoffBack"
    params = {'cause': cause, 'causeCate': causeCate, 'tipoffType': tipoffType, 'resId': resId}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
