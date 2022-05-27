#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Match_Controller.data_fixture import Match_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_MatchReview(object):
    """查看赛事列表(赛事回顾)"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/user/_guest/matchReview"
        self.headers = login_train[-1]

    @pytest.mark.parametrize('matchId',[Match_Controller().Match(0)[0],Match_Controller().Match(4)[0],Match_Controller().Match(6)[0],Match_Controller().Match(7)[0],None])
    def test_MatchReview(self,public,matchId):
        """
        查看赛事列表(赛事回顾)
        :param public:
        :return:
        """
        self.params = {
            "matchId":matchId,
            "page":1,
            "rows":15
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['matchId'] is not None:
            assert self.result['result'] == '0'
        # elif self.params['matchId'] is None:
        #     assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))









