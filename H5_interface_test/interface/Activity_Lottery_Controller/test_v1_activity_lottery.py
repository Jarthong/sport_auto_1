from db_fixture.getdata import GetData

__author__ = 'huxm855'

import os
import pytest
import requests

# 抽奖活动id,【None，随机获取存在，不存在(最大值+1，最小值-1)】
# 查询抽奖活动activity_status 活动状态（1=未开始|2=活动中|3=已结束|4=未发布）

normal_activity_id_status1 = GetData('activity_id', 'activity_base', 'where activity_status=1').result()
normal_activity_id_status2 = GetData('activity_id', 'activity_base', 'where activity_status=2').result()
normal_activity_id_status3 = GetData('activity_id', 'activity_base', 'where activity_status=3').result()
normal_activity_id_status4 = GetData('activity_id', 'activity_base', 'where activity_status=4').result()
max_activity_id = GetData('max(activity_id)', 'activity_base').result() + 1
min_activity_id = GetData('min(activity_id)', 'activity_base').result() - 1


@pytest.mark.parametrize('activity_id', [None,
                                         pytest.param(normal_activity_id_status1, marks=[
                                             pytest.mark.skipif(normal_activity_id_status1 == 0,
                                                                reason='没有找到未开始状态的活动')]),
                                         pytest.param(normal_activity_id_status2, marks=[
                                             pytest.mark.skipif(normal_activity_id_status2 == 0,
                                                                reason='没有找到活动中状态的活动')]),
                                         pytest.param(normal_activity_id_status3, marks=[
                                             pytest.mark.skipif(normal_activity_id_status3 == 0,
                                                                reason='没有找到已结束状态的活动')]),
                                         pytest.param(normal_activity_id_status4, marks=[
                                             pytest.mark.skipif(normal_activity_id_status4 == 0,
                                                                reason='没有找到已结束状态的活动')]),
                                         max_activity_id,
                                         min_activity_id],
                         ids=['None', 'normal1', 'normal2', 'normal3', 'normal4', 'max', 'min'])
def test_v1_activity_lottery(login, activity_id):
    ''' 抽奖'''
    base_url = login.host + "/v1/activity/lottery"
    params = {'id': activity_id}
    r = requests.post(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)

    if activity_id is None:
        assert result['result'] == '4002'
        assert result['msg'] == '参数错误[Long@id]'
    else:
        if activity_id is not None:
            activity_status = GetData('activity_status', 'activity_base',
                                      'where activity_id={activity_id}'.format(activity_id=activity_id)).result()
            if activity_status in (1, 4):
                assert result['msg'] == '活动未开始'
            elif activity_status == 2:
                assert result['msg'] in ('您今天已经没有抽奖机会了 明天可继续抽奖哦!','成功', '用户超过了最大抽奖次数')
                if result['msg'] == '成功':
                    assert result['data']['activityId'] == activity_id
                    assert result['data']['prizeName'] == '谢谢参与'
            elif activity_status == 3:
                assert result['msg'] == '活动已结束'
            else:
                assert result['result'] == '2'
                assert result['msg'] == '对照接口文档,检查接口必输参数是否有值或参数类型是否正确...'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
