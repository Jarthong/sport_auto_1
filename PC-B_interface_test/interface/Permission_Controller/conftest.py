import pytest

from db_fixture.common import GlobalVar
from db_fixture.login_token import login_token

__author__ = 'huxm855'

@pytest.fixture
def login_match(request):
    userInfo = login_token(phone=GlobalVar.GVar['match_org_phone'])
    yield userInfo

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)


@pytest.fixture
def login_train(request):
    userInfo = login_token(phone=GlobalVar.GVar['train_org_phone2'])
    yield userInfo

    def tear_down_def():
        print(' ;ENDING')

    request.addfinalizer(tear_down_def)