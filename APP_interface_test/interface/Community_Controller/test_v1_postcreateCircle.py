#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_PostCreateCircle(object):
    """创建我的圈子"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/circle/createcircle"
        self.headers = login_train[-1]

    def test_postcreatecircle(self,public):
        """
        创建我的圈子
        :param public:
        :return:
        """
        self.params = {
            "circleType":'2',
            "circleName":'嘻嘻哈哈讨论',
            "fileId":'22657',
            "summarize":"大家开心就好"
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '只能创建一个圈子'
        assert self.result['result'] == '17001'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



