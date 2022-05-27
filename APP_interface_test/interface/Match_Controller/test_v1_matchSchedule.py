#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Match_Controller.data_fixture import Match_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_MatchSchedule(object):
    """分页查看赛程列表"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/user/_guest/matchSchedule"
        self.headers = login_train[-1]

    matchId = [Match_Controller().Match_Chart('match_chart_basketball'),Match_Controller().Match_Chart('match_chart_badminton'),
               Match_Controller().Match_Chart('match_chart_football'),Match_Controller().Match_Chart('match_chart_pingpong'),
               Match_Controller().Match_Chart('match_chart_tennis'),None]
    status = [0,1,2,3,4,5,None]
    @pytest.mark.parametrize('matchId',matchId)
    @pytest.mark.parametrize('status',status)
    def test_matchschedule(self,public,matchId,status):
        """
        分页查看赛程列表
        :param public:
        :return:
        """
        self.params = {
            "matchId":matchId,
            "status":status,
            "inStatus":'',
            "grade":'',
            "page":1,
            "rows":15
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['matchId'] is not None:
            assert self.result['msg'] == '成功'
        elif self.params['matchId'] is None:
            assert '不能为null' in self.result['msg']
            assert self.result['result'] == '4002'





if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

