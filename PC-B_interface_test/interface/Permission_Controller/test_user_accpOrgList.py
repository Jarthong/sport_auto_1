import os

import pytest
import requests

from db_fixture.common import GlobalVar
from db_fixture.login_token import login_token

base_url = GlobalVar.GVar['host'] + "/user/accpOrgList"


def test_login_employee(login):
    '''个人用户 获取用户授权组织列表 '''
    r = requests.get(base_url, headers=login.headers)
    result = r.json()
    assert result['msg'] == '成功'
    assert result['result'] == '0'


def test_login_match(login_match):
    '''赛事组织用户 获取用户授权组织列表 '''
    r = requests.get(base_url, headers=login_match.headers)
    result = r.json()
    assert result['msg'] == '成功'
    assert result['result'] == '0'


def test_login_train(login_train):
    '''培训组织用户 获取用户授权组织列表 '''
    r = requests.get(base_url, headers=login_train.headers)
    result = r.json()
    assert result['msg'] == '成功'
    assert result['result'] == '0'


if __name__ == '__main__':
    os.system('pytest -s -v test_user_accpOrgList.py')
