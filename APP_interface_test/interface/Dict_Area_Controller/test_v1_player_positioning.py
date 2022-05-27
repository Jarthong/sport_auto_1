#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_Player_Positioning(object):
    """球员定位字基础数据查询接口"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/dict/player/positioning"
        self.headers = login_match[-1]

    def test_player_positioning(self,public):
        """
        球员位置基础数据查询接口
        :param public:
        :return:
        """
        self.params = {
            "lang":'zh_CN',
            "sportType":''
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))




