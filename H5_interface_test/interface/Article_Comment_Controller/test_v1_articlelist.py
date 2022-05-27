#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os

import pytest
import requests

from db_fixture.common import GlobalVar


class Test_Articlelist(object):
    """个人中心查看用户的资讯功能接口"""

    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/article/_guest/articleList"
        self.headers = login.headers

    publishStatus = [0, 1, None]
    userId = GlobalVar().GVar['user_id']

    @pytest.mark.parametrize('publishStatus', publishStatus)
    @pytest.mark.parametrize('userId', userId)
    def test_articlelist(self, public, publishStatus, userId):
        """
        个人中心查看用户的资讯功能接口
        :param public:
        :return:
        """
        self.params = {
            "userId": userId,
            "publishStatus": publishStatus,
            "pageNO": 1,
            "pageSize": 10
        }
        r = requests.get(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['publishStatus'] is not None:
            assert self.result['msg'] == '成功'
        elif self.params['publishStatus'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
