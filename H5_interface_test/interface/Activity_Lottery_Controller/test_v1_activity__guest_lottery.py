from db_fixture.getdata import GetData

__author__ = 'huxm855'

import os
import pytest
import requests

# 抽奖活动id,【None，随机获取存在，不存在(最大值+1，最小值-1)】
normal_activity_id = GetData('activity_id', 'activity_lottery_info').result()
max_activity_id = GetData('max(activity_id)', 'activity_lottery_info').result() + 1
min_activity_id = GetData('min(activity_id)', 'activity_lottery_info').result() - 1

@pytest.mark.parametrize('activity_id', [None, normal_activity_id, max_activity_id, min_activity_id], ids=['None', 'normal', 'max', 'min'])
def test_v1_activity__guest_lottery(login, activity_id):
    ''' 抽奖活动首页'''
    base_url = login.host + "/v1/activity/_guest/lottery"
    params = {'id': activity_id}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if activity_id is None:
        assert result['result'] == '4002'
        assert result['msg'] == '参数错误[Integer@id]'
    else:
        assert result['msg'] == '成功'
        if min_activity_id<activity_id<max_activity_id:
            #抽奖模板信息
            id,templateType,dialImg,backgroundImg=GetData('id,template_type,dial_img,background_img', 'activity_lottery_template',"where activity_id='{activity_id}'".format(activity_id=activity_id)).result()
            #抽奖名称
            activityName=GetData('activity_name', 'activity_base',"where activity_id='{activity_id}'".format(activity_id=activity_id)).result()
            #抽奖活动信息,参与人数
            isParticipatorShow,participatorShowNum,dayLotteryNum=GetData('is_participator_show,participator_show_num,day_lottery_num', 'activity_lottery_info',"where activity_id='{activity_id}'".format(activity_id=activity_id)).result()

            assert result['data']['id'] == id
            assert result['data']['templateType'] == templateType
            assert result['data']['dialImg'] == dialImg
            assert result['data']['backgroundImg'] == backgroundImg
            assert result['data']['activityName'] == activityName
            assert result['data']['isParticipatorShow'] == isParticipatorShow
            assert result['data']['participatorShowNum'] == participatorShowNum
            assert result['data']['dayLotteryNum'] == dayLotteryNum
        else:
            assert  'data' not in result.keys()



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))