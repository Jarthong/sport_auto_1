#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

status5 = [GetData(column='count(*)',table='goods_order',where="where BUYER_USER_ID = 'seedp546981' and `STATUS` = 5").result()]
status2 = [GetData(column='count(*)',table='goods_order',where="where BUYER_USER_ID = 'seedp546981' and `STATUS` = 2").result()]
status = [1,2,3,4,5,6,7,9]
@pytest.mark.parametrize('status',status)
def test_orderinfolist(login_hq,status):
    """
    获取订单列表
    :param public:
    :return:
    """
    base_url = login_hq.host + "/v1/order/orderInfoList"
    params = {
        'status':status,
        'page': 1,
        'rows':15
    }
    print(params)
    r = requests.get(base_url, headers=login_hq.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if status == 5:
        assert result['data']['total'] in status5 and  result['msg'] == '成功'
    elif status == 2:
        assert result['data']['total'] in status2 and result['msg'] == '成功'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



