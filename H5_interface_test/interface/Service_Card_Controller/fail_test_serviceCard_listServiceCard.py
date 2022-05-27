#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest

from  db_fixture.login_token import *


@pytest.mark.parametrize('state', [1, 3, 5, '$%^'])
@pytest.mark.parametrize('busType', [0])
def test_servicecard_listservicecard(login, busType, state):
    """
    获取服务卡列表
    busType:
    业务类型：0通用购买、1赛事、2培训、3票务
    state:
    1未激活 3已完成 5已终止
    :param public:
    :return:
    """
    base_url = login.host + "/v1/user/_guest/serviceCard/listServiceCard"
    params = {
        "busType": busType,
        "state": state,
        "page": 1,
        "rows": 10
    }
    r = requests.get(base_url, headers=login.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if params['state'] == 3:
        assert '优惠券-退款-PC0112' in result['data']['list'][1]['cardName']
    elif params['state'] == '$%^':
        assert '参数类型错误' in result['msg']
    elif params['state'] != '$%^':
        assert '成功' in result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
# list index out of range