#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os,re
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_Character_FootBall(object):
    """人物性格基础数据查询接口"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/dict/character/football"
        self.headers = login_match[-1]


    def test_character_football(self,public):
        """
        人物性格基础数据查询接口
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
        assert self.result['data']['remarks'] == '足球人物性格字典表'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



















