#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_GetAuthService(object):
    """获取IP的认证、服务功能,响应结果中key为authList是认证列表，key为serviceList是服务列表，key为queryList是查询列表，key为functionList是功能列表，
    key为settingsList是设置列表，key为interactiveList是互动列表"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/guest/getIpAuthService"
        self.headers = login_match[-1]


    def test_getauthservice(self,public):
        """
        获取IP的认证、服务功能,响应结果中key为authList是认证列表，key为serviceList是服务列表，key为queryList是查询列表，key为functionList是功能列表，
    key为settingsList是设置列表，key为interactiveList是互动列表
        :param public:
        :return:
        """
        self.params = {}
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))











