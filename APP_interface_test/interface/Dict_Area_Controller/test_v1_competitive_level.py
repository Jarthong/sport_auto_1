#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os,re
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_Competitive_Level(object):
    """竞技水平基础数据查询接口"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/dict/competitive/level"
        self.headers = login_match[-1]


    def test_competitive_level(self,public):
        """
        竞技水平基础数据查询接口
        :param public:
        :return:
        """
        self.params = {
            "lang":'zh_CN',
            "sportType":''
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,json=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['data']['remarks'] == '竞技水平字典表'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



















