#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Community_Controller.data_fixture import Community_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_circleDetail(object):
    """圈子详情"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/guest/circle/circleDetail"
        self.headers = login_train[-1]

    circleId = [Community_Controller().social_circle(),None]
    @pytest.mark.parametrize('circleId',circleId)
    def test_circledetail(self,public,circleId):
        """
        圈子详情
        :param public:
        :return:
        """
        self.params = {
            "circleId":circleId
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['circleId'] != None:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['circleId'] == None:
            assert self.result['result'] == '4002'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






