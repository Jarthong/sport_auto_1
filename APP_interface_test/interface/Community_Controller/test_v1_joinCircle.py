#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Community_Controller.data_fixture import Community_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_joinCircle(object):
    """加入圈子"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/circle/joinCircle"
        self.headers = login_train[-1]

    circleId = [Community_Controller().social_circle()[0],None]
    @pytest.mark.parametrize('circleId',circleId)
    def test_joinCircle(self,public,circleId):
        """
        加入圈子
        :param public:
        :return:
        """
        self.params = {
            "circleId":circleId
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if circleId is not None:
            assert self.result['result'] == '0'
            assert self.result['msg'] in( '请勿重复加入','成功')
        elif circleId is None:
            assert self.result['result'] == '4002'
            assert '参数错误' in self.result['msg']

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
