#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_checkCircleFeed(object):
    """查询圈子下的帖子"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/guest/circle/circleFeed"
        self.headers = login_train[-1]

    type = [1,2,3]
    @pytest.mark.parametrize('type',type)
    def test_checkcirclefeed(self,public,type):
        """
        查询圈子下的帖子,type:1、全部帖子；2、最新回复；3、精华帖
        :param public:
        :return:
        """
        self.params = {
            "circleId":"18485",
            "type":type,
            "page":"1",
            "rows":"10"
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))




