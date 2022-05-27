#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

orderNumber1 = [GetData(column='order_number',table='goods_order',where="where BUYER_USER_ID = 'seedp546981'").result()]
orderNumber2 = [GetData(column='order_number',table='goods_order',where="where BUYER_USER_ID != 'seedp546981'").result()]
orderNumber = [orderNumber1,orderNumber2,None,'*&^']
@pytest.mark.parametrize('orderNumber',orderNumber)

def test_orderinfo(login_hq, orderNumber):
    """
    获取订单
    :param public:
    :return:
    """
    base_url = login_hq.host + "/v1/order/orderInfo"
    params = {
        'orderNumber': orderNumber
    }
    print(params['orderNumber'])
    r = requests.get(base_url, headers=login_hq.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if params['orderNumber'] == orderNumber1:
        assert   result['data']['orderNumber'] is not None
        assert result['msg'] == '成功'
    elif params['orderNumber'] == orderNumber2:
        assert result['msg'] == '用户权限不足' and result['result'] == '1009'
    elif params['orderNumber'] == None:
        assert '参数错误' in result['msg']
    elif params['orderNumber'] == '*&^':
        assert result['result'] == '0'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

