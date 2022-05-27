#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import time
import pytest
import requests
from db_fixture.common import *
from db_fixture.getdata import *

id1 = (GetData('b.id','user_info a,train_teacher b',
             "a.user_id = b.created_id AND a.PHONE = {PHONE} AND b.`status` = {status}"
               .format(PHONE=GlobalVar.GVar_hq['user_phone2'],status=1)).result())

teacherId = [id1,None,'%^&']
@pytest.mark.parametrize('teacherId',teacherId)
def test_teacher_courseDetail(login_hq2,teacherId):
    """
    获取教练的课程详情
    :param public:
    :return:
    """
    base_url = login_hq2.host + "/train/teacher/courseDetail"
    params = {
        'teacherId':teacherId,
        'page':1,
        'rows':15
    }
    print(params)
    r = requests.get(base_url, headers=login_hq2.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if teacherId == None:
        assert '参数错误' in result['msg']
    elif teacherId == '%^&':
        assert '参数类型错误' in result['msg']
    elif teacherId == id1:
        assert result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))









