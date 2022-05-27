#!/user/bin/python
#encoding:utf-8

#__auth__=='__hq__'

import os,random
import time
import pytest
import requests
from db_fixture.common import *
from db_fixture.getdata import *


idNolist = [440308198601013698, 440308198601019774, 440308198601019934, 440308198601010438, 440102199901010777,
           440102199901018218, 440102199901016458, 440102199901013935, 440102199901018752, 440103198501010198,
           440103198501019192, 440103198501014359, 440103198501017138, 440103198501018296, 440105199901018938,
           440105199901018938, 440105199901012691, 440105199901019279, 440105199901016457, '44010519990101745x',
           440306199901017959, 440306199901013050, '44030619990101263x', 440306199901013237]
pho_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152","153",
            "155", "156", "157", "158", "159", "186", "187", "188"]
mobile = [random.choice(pho_list) + "".join(random.choice("0123456789") for i in range(8))]

@pytest.mark.parametrize('mobile',mobile)
def test_teacher_save_1(login_hq2,mobile):
    """
    证件号使用正确
    :return:
    """
    base_url = login_hq2.host + "/train/teacher/save"
    params = {
        "name":"autotest教练",
        "sex":"2",
        "nationality":"中国",
        "idType":1,
        "idNo":random.choice(idNolist),
        "mobile":mobile
    }
    r = requests.post(base_url,headers=login_hq2.headers,verify=False,params=params)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['result'] == '0'



idNo = [GetData('c.card_id','user_info a,train_teacher b,biz_sensitive c',
                'a.user_id = b.created_id AND b.SID = c.ID AND a.phone = {phone} and b.`status` = 1'
               .format(phone=GlobalVar.GVar_hq['user_phone2'])).result(),None,123456789]
pho_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152","153",
            "155", "156", "157", "158", "159", "186", "187", "188"]
mobile = [random.choice(pho_list) + "".join(random.choice("0123456789") for i in range(8))]
@pytest.mark.parametrize('idNo',idNo)
@pytest.mark.parametrize('mobile',mobile)
def test_teacher_save_same(login_hq2,idNo,mobile):
    """
    证件号重复使用
    :return:
    """
    base_url = login_hq2.host + "/train/teacher/save"
    params = {
        "name":"autotest教练",
        "sex":"2",
        "nationality":"中国",
        "idType":1,
        "idNo":idNo,
        "mobile":mobile
    }
    r = requests.post(base_url,headers=login_hq2.headers,verify=False,params=params)
    result = r.json()
    print(result)
    if idNo != None and idNo != 123456789:
        assert result['msg'] == '该证件号已存在'
        assert result['result'] == '40025'
    else:
        if idNo == None:
            assert '证件号不能为空' in result['msg']
            assert result['result'] == '40027'
        elif idNo == 123456789:
            assert result['msg'] == '身份证无效'
            assert result['result'] == '2126'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

