#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests

def test_refundReason(login_hq):
    """
    获取退款原因
    :param public:
    :return:
    """
    base_url = login_hq.host + "/v1/order/refundReason"
    params = {}
    r = requests.get(base_url, headers=login_hq.headers, verify=False, params=params)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert '收货人信息有误' in result['data'][0]['refundReasonDesc']
    assert '我不想买了' in result['data'][1]['refundReasonDesc']
    assert '重复下单/误下单' in result['data'][2]['refundReasonDesc']
    assert '其他原因' in result['data'][3]['refundReasonDesc']



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))




