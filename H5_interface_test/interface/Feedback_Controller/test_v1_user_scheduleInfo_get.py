import datetime

__author__ = 'huxm855'

import os
import requests
year=datetime.date.today().year
month=datetime.date.today().month
day =datetime.date.today().day
def test_v1_user_scheduleInfo(login):
    ''' 查询用户的日程详情信息列表接口'''
    base_url =login.host + "/v1/user/scheduleInfo"
    params={'eventDate':str(year)+'-'+str(month)+'-'+str(day)}
    r = requests.get(base_url, headers=login.headers, params=params,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))