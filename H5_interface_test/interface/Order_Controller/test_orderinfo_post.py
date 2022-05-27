#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

sku_Code1 = (GetData(column='b.SKU_CODE',table='goods a,goods_sku b,`match` c',where='where a.GOODS_CODE = b.GOODS_CODE AND b.GOODS_CODE = c.GOODS_CODE AND a.`STATUS` = 0 AND a.CHECK_STATUS = 1 AND c.`STATUS` = 1').result())
sku_Code2 = (GetData(column='b.SKU_CODE', table='goods a,goods_sku b,`match` c',where='where a.GOODS_CODE = b.GOODS_CODE AND b.GOODS_CODE = c.GOODS_CODE AND a.`STATUS` = 1 AND a.CHECK_STATUS = 1 AND c.`STATUS` = 2').result())
sku_Code3 = (GetData(column='b.SKU_CODE',table='goods a,goods_sku b',where='where a.GOODS_CODE = b.GOODS_CODE and a.`STATUS` = 1 AND a.CHECK_STATUS = 2').result())
sku_Code4 = (GetData(column='b.SKU_CODE', table='goods a,goods_sku b,`match` c',where='where a.GOODS_CODE = b.GOODS_CODE AND b.GOODS_CODE = c.GOODS_CODE AND a.`STATUS` = 0 AND a.CHECK_STATUS = 1 AND c.`STATUS` = 4').result())

skuCode = [sku_Code1,sku_Code2,sku_Code3,sku_Code4,None]
quantity = [0,1]
addressId1 = (GetData(column='ID',table='user_delivery_address',where="where user_id = 'seedp546981'").result())
addressId = [addressId1,None,'^&*']
@pytest.mark.parametrize('addressId',addressId)
@pytest.mark.parametrize('skuCode', skuCode)
@pytest.mark.parametrize('quantity',quantity)

def test_orderinfo(login_hq, addressId, skuCode,quantity):
    """
    创建（商品）订单，非砍价订单
    BUY_STATUS'购买状态：0 不能购买，1能购买'
    STATUS'0：无效，1：有效'
    :param public:
    :return:
    """
    base_url = login_hq.host + "/v1/order/orderInfo"
    params = {
        "addressId": addressId,
        "detailList[0].skuCode": str(skuCode),
        "detailList[0].quantity":quantity
    }
    print(params['detailList[0].skuCode'])
    r = requests.post(base_url, headers=login_hq.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if skuCode == None and quantity == 1 and addressId == addressId1:
        assert result['msg'] == '商品不存在' and result['result'] == '20027'
    else:
        if params['detailList[0].skuCode'] == sku_Code1 and quantity == 1 and addressId != '^&*':
            assert '抱歉，预热中的商品暂不能购买' in result['msg'] and '20046' in result['result']
        elif params['detailList[0].skuCode'] == sku_Code2 and quantity == 1 and addressId != '^&*':
            assert '该商品已经下架' in result['msg'] and '20034' in result['result']
        elif params['detailList[0].skuCode'] == sku_Code3 and quantity == 1 and addressId != '^&*':
            assert '该商品未审核通过' in result['msg'] and '20056' in result['result']
        elif quantity == 0 and addressId != '^&*' and addressId != '^&*':
            assert '最小不能小于1' in result['msg']
        elif params['detailList[0].skuCode'] == sku_Code4 and quantity == 1 and addressId != '^&*':
            try:
                assert result['data']['status'] == 9 and result['msg'] == '成功'
            except:
                print('商品限制问题，购买次数限制')


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

