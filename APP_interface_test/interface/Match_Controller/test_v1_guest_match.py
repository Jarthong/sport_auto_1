#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Match_Controller.data_fixture import *
from interface.Community_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_GuestMatch(object):
    """查看赛事列表（进行中的赛事）"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/user/_guest/match"
        self.headers = login_train[-1]

    @pytest.mark.parametrize('userId',['seedp545121'])
    def test_Guestmatch(self,public,userId):
        """
        查看赛事列表（进行中的赛事）
        :param public:
        :return:
        """
        self.params = {
            "userId":userId,
            "page":1,
            "rows":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['userId'] is not None:
            assert self.result['result'] == '0'




if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))








