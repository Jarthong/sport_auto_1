#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests

from db_fixture.common import GlobalVar
from interface.Social_Circle_Controller.data_fixture import Social_Controller


class Test_SocialCircle_Guest_Members(object):
    """查询所有成员"""

    @pytest.fixture()
    def public(self, login_hq2):
        self.base_url = login_hq2.host + "/v1/socialCircle/_guest/members"
        self.headers = login_hq2.headers

    id = [Social_Controller().social_circle(GlobalVar().GVar_hq['user_id2']), None, '$%^']

    @pytest.mark.parametrize('id', id)
    def test_guest_members(self, public, id):
        """
        查询所有成员
        :param public:
        :return:
        """
        self.params = {
            "id": id
        }
        r = requests.get(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['id'] is not None and self.params['id'] != '$%^':
            assert '成功' in self.result['msg']
        elif self.params['id'] is None:
            assert '参数错误' in self.result['msg']
        elif self.params['id'] == '$%^':
            assert '参数类型错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
