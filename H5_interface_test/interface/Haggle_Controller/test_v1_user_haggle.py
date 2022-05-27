__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from db_fixture.common import GlobalVar
from db_fixture.getdata import *

#已发布且未发起过砍价的活动ID
haggleId_not =  GetData('ID', 'haggle_activity', " where ID NOT IN (SELECT haggle_id FROM haggle_initiator WHERE INITIATOR_ID ='{INITIATOR_ID}') AND HAGGLE_STATUS = 1".format(INITIATOR_ID= GlobalVar.GVar_hq['c_user_id'])).result()
#未发起砍价的用户
initiatorId_not = GetData('USER_ID', 'user_info', 'where USER_ID not in (SELECT INITIATOR_ID FROM haggle_initiator WHERE haggle_id = {haggle_id})'.format(haggle_id= haggleId_not)).result()
#已发起砍价的用户
initiatorId_done = GetData('INITIATOR_ID', 'haggle_initiator', 'where haggle_id = {haggle_id}'.format(haggle_id= haggleId_not)).result()
#先查询出HAGGLE_INITIATOR_ID，再通过HAGGLE_INITIATOR_ID查询出该活动的所有已经砍价的用户
HAGGLE_INITIATOR_ID = GetData('id', 'haggle_initiator', "where INITIATOR_ID='{INITIATOR_ID}' AND haggle_id = {haggle_id} ".format(INITIATOR_ID= initiatorId_done, haggle_id= haggleId_not)).result()
HAGGLE_USER_ID = GetData('HAGGLE_USER_ID','haggle_record', 'where HAGGLE_INITIATOR_ID = {HAGGLE_INITIATOR_ID}'.format(HAGGLE_INITIATOR_ID=HAGGLE_INITIATOR_ID)).results()

#砍价价格
HAGGLE_PRICE = GetData('HAGGLE_PRICE','haggle_activity','where ID={ID}'.format(ID=haggleId_not)).result()
#砍价上限
UPPER_LIMIT_PRICE = GetData('UPPER_LIMIT_PRICE','haggle_activity','where ID={ID}'.format(ID=haggleId_not)).result()
#商品销售价格
GOODS_PRICE = GetData(column='GOODS_SALE_PRICE', table='goods t1, haggle_activity t2', where='where t1.GOODS_CODE = t2.GOODS_CODE AND t2.ID = {ID}'.format(ID=haggleId_not)).result()
#砍价发起人在这个活动的砍价总额
sum_HAGGLE_PRICE = GetData(column='sum(HAGGLE_PRICE)', table='haggle_record',where="where HAGGLE_INITIATOR_ID='{HAGGLE_INITIATOR_ID}'".format(HAGGLE_INITIATOR_ID=HAGGLE_INITIATOR_ID)).result()

haggleId = [None, haggleId_not]
initiatorId = [None, 0 , initiatorId_not, initiatorId_done]
@pytest.mark.parametrize('initiatorId', initiatorId)
@pytest.mark.parametrize('haggleId', haggleId)
def test_v1_user_haggle(login_c, haggleId, initiatorId):
    """
    砍价
    :param haggleId: 砍价活动ID
    :param initiatorId: 砍价发起人
    :return:
    """
    base_url = login_c.host + "/v1/user/haggle"
    print(base_url)
    params = {'haggleId': haggleId,
              'initiatorId':initiatorId}
    print("params:",params)
    r = requests.post(base_url, headers=login_c.headers, data=params, verify=False)
    result = r.json()
    print(result)
    if haggleId == None or initiatorId == None:
        assert '参数错误' in result['msg']

    elif initiatorId == 0:
        assert result['msg'] == '该砍价发起人不存在'

    elif initiatorId == initiatorId_not :
        assert result['msg'] == '该用户尚未发起过砍价，不能砍价'

    elif GlobalVar.GVar_hq['c_user_id'] in HAGGLE_USER_ID:
        assert result['msg'] == '该用户已经参与此砍价活动'

    else:
        if GlobalVar.GVar_hq['c_user_id'] not in HAGGLE_USER_ID and GOODS_PRICE>10 and sum_HAGGLE_PRICE >= UPPER_LIMIT_PRICE:
            assert result['msg'] == '已经砍到上限金额'

        elif GlobalVar.GVar_hq['c_user_id'] not in HAGGLE_USER_ID and (GOODS_PRICE<10 or (GOODS_PRICE - HAGGLE_PRICE)<10):
            assert result['msg'] == '单次砍价金额不能小于一毛钱'

        else:
            assert result['msg'] == '成功'







if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
