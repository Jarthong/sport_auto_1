#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import os
import pytest
import requests


class Test_SocialCircle_Guest_index(object):
    """社区首页"""

    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/socialCircle/_guest/index"
        self.headers = login.headers

    def test_guest_index(self,public):
        """
        社区首页
        :param public:
        :return:
        """
        r = requests.get(self.base_url,headers = self.headers,verify=False)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






