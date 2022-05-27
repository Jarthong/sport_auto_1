#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests

from interface.Match_Controller.data_fixture import Match_Controller


class Test_MatchNotice(object):
    """查看赛事公告信息列表"""

    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/_guest/matchNotice"
        self.headers = login.headers

    matchId = [Match_Controller().match(), None, '%^&']

    @pytest.mark.parametrize('matchId', matchId)
    def test_matchnotice(self, public, matchId):
        """
        查看赛事公告信息列表
        :param public:
        :return:
        """
        self.params = {
            "matchId": matchId
        }
        r = requests.get(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['matchId'] is not None and self.params['matchId'] != '%^&':
            assert self.result['msg'] == '成功'
        elif self.params['matchId'] is None:
            assert '参数错误' in self.result['msg']
        elif self.params['matchId'] == '%^&':
            assert '参数类型错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
