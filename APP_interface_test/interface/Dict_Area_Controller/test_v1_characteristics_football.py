#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os,re
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_Characteristic_FootBall(object):
    """人物能力特征基础数据查询接口"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/dict/characteristics/football"
        self.headers = login_match[-1]


    def test_characteristic_football(self,public):
        """
        人物能力特征基础数据查询接口
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
        assert self.result['data']['remarks'] == '足球人物能力特征字典表'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



















