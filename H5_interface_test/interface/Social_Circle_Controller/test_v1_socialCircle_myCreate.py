#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests


class Test_SocialCircle_myCreate(object):
    """查询用户创建的所有圈子接口"""
    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/socialCircle/myCreate"
        self.headers = login.headers

    def test_guest_myCreate(self, public):
        """
        查询用户创建的所有圈子接口
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


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
