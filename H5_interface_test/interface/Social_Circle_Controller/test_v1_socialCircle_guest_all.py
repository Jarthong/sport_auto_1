#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os

import pytest
import requests


class Test_SocialCircle_Guest_All(object):
    """查询所有圈子不包含我创建与我加入的"""

    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/socialCircle/_guest/all"
        self.headers = login.headers

    def test_guest_all(self, public):
        """
        查询所有圈子不包含我创建与我加入的
        :param public:
        :return:
        """
        self.params = {
            "page": 1,
            "rows": 10
        }
        r = requests.get(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'
        assert self.result['result'] == '0'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
