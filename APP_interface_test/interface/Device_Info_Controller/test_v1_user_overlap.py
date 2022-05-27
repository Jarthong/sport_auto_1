__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
from datetime import date, timedelta
import pytest
import requests


@pytest.mark.parametrize('startTime',[str(date.today() + timedelta(days=1)),None])
@pytest.mark.parametrize('endTime',[str(date.today() + timedelta(days=16)),None])
def test_v1_user_overlap(login,startTime,endTime):
    ''' 检查日程冲突'''
    base_url =login[0] + "/v1/user/overlap"
    params={'startTime':startTime,'endTime':endTime}
    r = requests.get(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if startTime==None or endTime==None:
        assert result['result']==  '4002'
    else:
        assert result['result']==  '0'



if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
