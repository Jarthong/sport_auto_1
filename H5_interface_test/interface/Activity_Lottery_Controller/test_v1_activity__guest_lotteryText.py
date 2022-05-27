import time

from db_fixture.getdata import GetData

__author__ = 'huxm855'

import os
import pytest
import requests

# 抽奖活动id,【None，随机获取存在，不存在(最大值+1，最小值-1)】
normal_activity_id = GetData('activity_id', 'activity_base').result()
max_activity_id = GetData('max(activity_id)', 'activity_base').result() + 1
min_activity_id = GetData('min(activity_id)', 'activity_base').result() - 1

@pytest.mark.parametrize('activity_id', [None, normal_activity_id, max_activity_id, min_activity_id],
                         ids=['None', 'normal', 'max', 'min'])
def test_v1_activity__guest_lotteryText(login, activity_id):
    ''' 活动说明'''
    base_url = login.host + "/v1/activity/_guest/lotteryText"
    params = {'id': activity_id}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if activity_id is None:
        assert result['result'] == '4002'
        assert result['msg'] == '参数错误[Integer@id]'
    else:
        assert result['msg'] == '成功'
        if min_activity_id < activity_id < max_activity_id:
            # 抽奖活动信息,活动描述，开始，结束时间
            activityDec, activityStart, activityEnd = GetData('activity_dec,activity_start,activity_end',
                                                              'activity_base',
                                                              "where activity_id='{activity_id}'".format(
                                                                  activity_id=activity_id)).result()
            activity_Start = int(time.mktime(time.strptime(str(activityStart), "%Y-%m-%d %H:%M:%S")) * 1000)
            activity_End = int(time.mktime(time.strptime(str(activityEnd), "%Y-%m-%d %H:%M:%S")) * 1000)
            assert result['data']['activityDec'] == activityDec
            assert result['data']['activityStart'] == activity_Start
            assert result['data']['activityEnd'] == activity_End

        else:
            assert 'data' not in result.keys()


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
