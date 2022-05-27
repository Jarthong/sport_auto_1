#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Community_Controller.data_fixture import Community_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_Disbaled(object):
    """检查圈子名字是否可用"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/circle/circleDisabled"
        self.headers = login_train[-1]

    circleId = [18485,None]
    userList = [Community_Controller().circle_member(18485,'seedp543681')[2]]
    isUsed = [1,2]
    @pytest.mark.parametrize('circleId',circleId)
    @pytest.mark.parametrize('userList',userList)
    @pytest.mark.parametrize('isUsed',isUsed)
    def test_disabled(self,public,circleId,userList,isUsed):
        """
        检查圈子名字是否可用
        :param public:
        :return:
        """
        self.params = {
            "circleId":circleId,
            "isUsed":isUsed,
            "userList":userList
        }
        print(self.params)
        a = print(self.params)
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['circleId'] != None:
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'
        elif self.params['circleId'] == None:
            assert self.result['msg'] == '接口异常（通用错误）'
            assert self.result['result'] == '1000'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



