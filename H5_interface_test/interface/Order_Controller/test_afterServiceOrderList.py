#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests

def test_afterserviceorderlist(login_hq):
    """
    获取订单售后申请列表
    :param public:
    :return:
    """
    base_url = login_hq.host + "/v1/order/afterServiceOrderList"
    params = {
        'page': 1,
        'rows':15
    }
    r = requests.get(base_url, headers=login_hq.headers, verify=False, params=params)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data']['page'] == 1 or result['data']['rows'] == 15


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


