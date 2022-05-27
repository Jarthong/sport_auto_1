__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import pytest
import os
import requests
from db_fixture.login_token import *
from db_fixture.common import GlobalVar
from db_fixture.getdata import *

#未发布的活动ID
haggleId_unpublished = GetData('ID', 'haggle_activity', where='where HAGGLE_STATUS = 0').result()
#已发布且未发起过砍价的活动ID
haggleId_effective =  GetData('ID', 'haggle_activity', where="where ID NOT IN (SELECT haggle_id FROM haggle_initiator WHERE INITIATOR_ID ='{INITIATOR_ID}') AND HAGGLE_STATUS = 1".format(INITIATOR_ID= GlobalVar.GVar_hq['c_user_id'])).result()
#已发布但已发起过砍价的活动ID
haggleId_invalid = GetData('ID', 'haggle_activity', where="where ID IN (SELECT haggle_id FROM haggle_initiator WHERE INITIATOR_ID ='{INITIATOR_ID}') AND HAGGLE_STATUS = 1".format(INITIATOR_ID= GlobalVar.GVar_hq['c_user_id'])).result()
#已结束的活动ID
haggleId_end=  GetData('ID', 'haggle_activity', where='where HAGGLE_STATUS = 2').result()


haggleId = [None, 0, haggleId_unpublished, haggleId_end, haggleId_invalid, haggleId_effective]
@pytest.mark.parametrize('haggleId', haggleId)
def test_v1_user_initiateHaggle(login_c, haggleId):
    """
    发起砍价
    :param haggleId: 砍价活动ID
    :return:
    """
    base_url = login_c.host + "/v1/user/initiateHaggle"
    print(base_url)
    params = {'haggleId': haggleId}
    print("params:",params)
    r = requests.post(base_url, headers=login_c.headers, data=params, verify=False)
    result = r.json()
    print(result)
    if haggleId == None:
        assert '参数错误' in result['msg']

    elif haggleId == 0:
        assert result['msg'] == '该砍价活动不存在'

    elif haggleId == haggleId_unpublished:
        assert result['msg'] == '该砍价活动未发布'

    elif haggleId == haggleId_end:
        assert result['msg'] == '该砍价活动已经结束，操作失败'

    elif haggleId == haggleId_invalid:
        assert result['msg'] == '该用户已发起过砍价'

    else:
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
