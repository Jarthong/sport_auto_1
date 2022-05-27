from db_fixture.common import GlobalVar
from db_fixture.login_token import login_token

__author__ = 'huxm855'
import pytest



@pytest.fixture(scope="function")
def login(request):
    host, userId, headers = login_token(phone=GlobalVar.GVar_hxm['user_phone2'],password=GlobalVar.GVar_hxm['passworld']).userInfo()

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)

    return host, userId, headers

