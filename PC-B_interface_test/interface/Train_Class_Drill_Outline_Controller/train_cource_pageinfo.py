#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests
from db_fixture.common import *
from db_fixture.getdata import *

teacherId = [None,GetData('b.ID','user_info a,train_teacher b,biz_sensitive c',
                     'a.user_id = b.created_id and b.SID = c.ID and a.phone = {phone} and b.`status` = {status}'
                     .format(phone=GlobalVar.GVar_hq['user_phone2'],status=1)).result()]
courseStatus = [1,2,4,5]
@pytest.mark.parametrize('courseStatus',courseStatus)
@pytest.mark.parametrize('teacherId',teacherId)
def test_trainCoursePageInfo(login_hq2,teacherId,courseStatus):
    """
    课程详情
    :param public:
    :return:
    """
    base_url = login_hq2.host + "/train/course/trainCoursePageInfo"
    params = {
        'page':1,
        'rows':15,
        'teacherId':teacherId,
        'courseStatus':courseStatus
    }
    r = requests.get(base_url, headers=login_hq2.headers, verify=False, params=params)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

