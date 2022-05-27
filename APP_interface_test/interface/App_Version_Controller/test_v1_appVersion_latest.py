# encoding:utf-8
import heapq
from operator import itemgetter

from db_fixture.getdata import GetData

__author__ = 'huxm855'

import os
import pytest
import requests

deviceType = list(range(2, 4))
deviceType.append(None)


@pytest.mark.parametrize('deviceType', deviceType)
def test_v1_appVersion_latest(login, deviceType):
    ''' 查询最新版本号'''
    base_url = login[0] + "/v1/appVersion/latest"
    params = {'deviceType': deviceType}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if deviceType != None:
        assert result['msg'] == '成功'
        sql_result = GetData(
            sql='select version,version_name,create_time from app_version  where device_type={device_type}'.format(device_type=deviceType)).results_querys()
        try:
            order_value=heapq.nlargest(1, sql_result, key=lambda x: (int(x['version']),x['create_time']))[0]
        except:
            order_value=heapq.nlargest(1, sql_result, key=itemgetter('create_time'))[0]
        print(order_value)

        assert result['data']['version'] == order_value['version']
        assert result['data']['versionName'] == order_value['version_name']
    else:
        assert result['result'] == '4002'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
