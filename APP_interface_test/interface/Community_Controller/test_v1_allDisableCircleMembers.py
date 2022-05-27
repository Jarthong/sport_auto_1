#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest
from db_fixture.login_token import *
from interface.Article_Comment_Contro.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_allDisableCircleMembers(object):
    """查询圈子所有被禁用成员"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/circle/allDisableCircleMembers"
        self.headers = login_train[-1]


    def test_allDisableCircleMembers(self,public):
        """
        查询圈子所有被禁用成员
        :param public:
        :return:
        """
        self.params = {
            "circleId": 18485,
            "page":1,
            "rows":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'
        assert self.result['result'] == '0'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

