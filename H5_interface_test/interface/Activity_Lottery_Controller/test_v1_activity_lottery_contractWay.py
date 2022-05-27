from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'

import pytest
import requests

# 抽奖活动id,【None，随机获取存在，不存在(最大值+1，最小值-1)】
normal_activity_id, redeemCode = GetData('activity_id,redeem_code', 'activity_lottery_winning_record',
                                         "where user_id='{userid}'".format(userid=GlobalVar.GVar['user_id'])).result()


@pytest.mark.parametrize('activityId', [None, normal_activity_id])
@pytest.mark.parametrize('redeemCode', [None, redeemCode])
@pytest.mark.parametrize('name', [None, 'landy'])
@pytest.mark.parametrize('phone', [None, GlobalVar.GVar['user_phone'], '1234567'])
@pytest.mark.parametrize('deliveryAddress', [None, '广东省深圳市福田区讯美大厦'])
def test_v1_activity_lottery_contractWay(login, activityId, redeemCode, name, phone, deliveryAddress):
    ''' 填写资料领取奖品'''
    base_url = login.host + "/v1/activity/lottery/contractWay"
    params = {'activityId': activityId, 'redeemCode': redeemCode, 'name': name, 'phone': phone,
              'deliveryAddress': deliveryAddress}
    r = requests.post(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if activityId is None or redeemCode is None or name is None or phone in (
    None, '1234567') or deliveryAddress is None:
        assert result['result'] in ('1000', '73', '4002')
    else:
        assert result['result'] == '0'


if __name__ == '__main__':
    pytest.main(['-x', __file__])
