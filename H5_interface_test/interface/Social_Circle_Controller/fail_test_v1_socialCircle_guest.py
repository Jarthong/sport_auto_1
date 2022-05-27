#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'
import os

import pytest
import requests

from db_fixture.common import GlobalVar
from interface.Social_Circle_Controller.data_fixture import Social_Controller



class Test_SocialCircle_Guest(object):
    """根据ID查询圈子"""

    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/socialCircle/_guest"
        self.headers = login.headers

    id = [Social_Controller().social_circle(GlobalVar().GVar['user_id']), None, '$%^%$$']

    @pytest.mark.parametrize('id', id)
    def test_guest(self, public, id):
        """
        根据ID查询圈子
        :param public:
        :return:
        """
        self.params = {
            "id": id
        }
        r = requests.get(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['id'] is not None and self.params['id'] != '$%^%$$':
            assert self.result['msg'] == '成功'
        elif self.params['id'] is None:
            assert '参数错误' in self.result['msg']
        elif self.params['id'] == '$%^%$$':
            assert '参数类型错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

    #该账号没数据导致用例失败
