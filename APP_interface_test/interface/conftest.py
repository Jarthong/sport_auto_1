#!/user/bin/python
#encoding:utf-8

import pytest
import requests

from db_fixture.common import *
from db_fixture.login_token import login_token

@pytest.fixture(scope="function")
def login_train(request):
    host,userId,headers = login_token(phone=GlobalVar.GVar_hq['train_org_phone']).userInfo()

    return host,userId,headers

@pytest.fixture(scope="function")
def login_match(request):
    host,userId,headers = login_token(phone=GlobalVar.GVar_hq['match_org_phone']).userInfo()

    return host,userId,headers

@pytest.fixture(scope="function")
def login_2(request):
    host,userId,headers = login_token(phone=GlobalVar.GVar_hq['phone_2']).userInfo()

    return host,userId,headers

@pytest.fixture(scope="function")
def login(request):
    host, userId, headers = login_token(phone=GlobalVar.GVar_hxm['user_phone'],password=GlobalVar.GVar_hxm['passworld']).userInfo()
    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)

    return host, userId, headers


@pytest.fixture(scope="function")
def login_chh(request):
    host, userId, headers = login_token(phone=GlobalVar.GVar_chh['user_phone'],password=GlobalVar.GVar_chh['user_password']).userInfo()

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)

    return host, userId, headers