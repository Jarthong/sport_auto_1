#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Community_Controller.data_fixture import Community_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_CheckCircleName(object):
    """检查圈子名字是否可用"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/circle/checkCircleName"
        self.headers = login_train[-1]

    circleName = [Community_Controller().social_circle()[1],None,'autotestname']
    @pytest.mark.parametrize('circleName',circleName)
    def test_checkcirclename(self,public,circleName):
        """
        检查圈子名字是否可用
        :param public:
        :return:
        """
        self.params = {
            "circleName": circleName
        }
        print(self.params)
        a = print(self.params)
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params == None:
            assert '参数错误' in self.result['msg']
            assert self.result['result'] == 4002
        elif self.params == 'autotestname':
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'
        elif a != None and a != 'autotestname':
            assert self.result['msg'] == '圈子名字已存在'
            assert self.result['result'] == '17002'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


