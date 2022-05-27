#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_preCreatecircle(object):
    """预创建我的圈子，判断是否有权限创建及消息告知"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/circle/preCreatecircle"
        self.headers = login_train[-1]

    def test_preCreatecircle(self,public):
        """
        预创建我的圈子，判断是否有权限创建及消息告知
        :param public:
        :return:
        """
        self.params = {}
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '只能创建一个圈子'
        assert self.result['result'] == '17001'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






