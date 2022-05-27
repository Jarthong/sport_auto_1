#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_myJoinCircle(object):
    """我加入的圈子"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/circle/myJoinCircle"
        self.headers = login_train[-1]

    def test_myJoinCircle(self,public):
        """
        我加入的圈子
        :param public:
        :return:
        """
        self.params = {
            "page":1,
            "rows":20
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






