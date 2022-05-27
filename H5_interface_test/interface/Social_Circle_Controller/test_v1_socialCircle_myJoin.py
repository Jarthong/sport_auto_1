#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests


class Test_SocialCircle_myJoin(object):
    """查询用户加入的圈子列表"""
    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/socialCircle/myJoin"
        self.headers = login.headers


    def test_guest_myjoin(self, public):
        """
        查询用户加入的圈子列表
        :param public:
        :return:
        """
        r = requests.get(self.base_url, headers=self.headers, verify=False)
        self.result = r.json()
        print(self.result)


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
