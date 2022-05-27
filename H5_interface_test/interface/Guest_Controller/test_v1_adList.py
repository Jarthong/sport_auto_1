#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests

showPosition = [24,41,42,43,44,45]
adsType = ['banner','screen','startPage']
@pytest.mark.parametrize('showPosition',showPosition)
@pytest.mark.parametrize('adsType',adsType)
def test_adList(login_hq3,adsType,showPosition):
    """
    获取广告列表
    :param public:
    :return:
    """
    base_url = login_hq3.host + "/v1/guest/adList"
    params = {
        'adsType':adsType,
        'showPosition':showPosition,
        'page':1,
        'rows':15
    }
    print(params)
    r = requests.get(base_url, headers=login_hq3.headers, verify=False, params=params)
    result = r.json()
    print(result)
    # results = result['data']['list']
    # list_results = [item[key] for item in results for key in item]
    # print(list_results)
    if adsType == 'banner' and showPosition == 24:
        assert result['msg'] == '成功'
    elif adsType == 'banner' and showPosition == 41:
        assert result['msg'] == '成功'
    elif adsType == 'banner' and showPosition == 42:
        assert result['data']['startRow'] == 1
    elif adsType == 'banner' and showPosition == 45:
        assert result['data']['total'] == 1
        assert '篮球-赛事-砍价-0417' in ([item[key] for item in result['data']['list'] for key in item])

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))







