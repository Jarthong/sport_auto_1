#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_Select_Banner(object):
    """获取直播轮播"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/_guest/liveRadio/streamException"
        self.headers = login_match[-1]


    def test_select_banner(self,public):
        """
        获取直播轮播
        :param public:
        :return:
        """
        self.params = {
            "liveId":''
        }
        print(self.params)
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))









