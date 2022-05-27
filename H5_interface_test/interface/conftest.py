import pytest

from db_fixture.common import GlobalVar
from db_fixture.login_token import login_token

@pytest.fixture
def login(request):
    userInfo = login_token()
    yield userInfo

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)
	
@pytest.fixture
def login_hq(request):
    userInfo = login_token(GlobalVar().GVar_hq['user_phone'],GlobalVar().GVar_hq['password'])
    yield userInfo

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)

@pytest.fixture
def login_hq2(request):
    userInfo = login_token(GlobalVar().GVar_hq['user_phone2'],GlobalVar().GVar_hq['password'])
    yield userInfo

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)

@pytest.fixture
def login_hq3(request):
    userInfo = login_token(GlobalVar().GVar_hq['user_phone3'],GlobalVar().GVar_hq['password'])
    yield userInfo

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)
	
@pytest.fixture(scope="function")
def login_c(request):
    userInfo = login_token(phone=GlobalVar.GVar_hq['c_user_phone'],password=GlobalVar.GVar_hq['c_password'], host=GlobalVar.GVar['host'])
    yield userInfo

    def tear_down_def():
        print(' ;ENDING')
        print('-------------------------------------------------------------------------')

    request.addfinalizer(tear_down_def)
