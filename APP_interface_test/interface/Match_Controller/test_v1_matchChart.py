#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Match_Controller.data_fixture import *
from interface.Community_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_MatchChart(object):
    """分页查看赛事排名"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/user/_guest/matchChart"
        self.headers = login_train[-1]

    matchId = [Match_Controller().Match_Chart('match_chart_basketball'),Match_Controller().Match_Chart('match_chart_badminton'),
               Match_Controller().Match_Chart('match_chart_football'),Match_Controller().Match_Chart('match_chart_pingpong'),
               Match_Controller().Match_Chart('match_chart_tennis'),2275,None]

    @pytest.mark.parametrize('matchId',matchId)
    def test_matchChart(self,public,matchId):
        """
        分页查看赛事排名
        :param public:
        :return:
        """
        self.params = {
            "matchId":matchId,
            "page":1,
            "rows":15
        }
        # print(self.params)
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['matchId'] is not None and self.params['matchId'] != 2275:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['matchId'] is None:
            assert '不能为null' in self.result['msg']
            assert self.result['result'] == '4002'
        elif self.params['matchId'] == 2275:
            assert '该赛事类型暂没有排名' in self.result['msg']
            assert self.result['result'] == '9028'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
