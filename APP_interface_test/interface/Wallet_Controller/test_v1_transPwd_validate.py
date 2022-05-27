#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_TransPwd_Validate(object):
    """验证交易密码"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/wallet/transPwd/validate"
        self.headers = login_match[-1]

    transPwd = [Encrypt().md5Encode("905987"),'1545154']
    @pytest.mark.parametrize('transPwd',transPwd)
    def test_transpwd_validate(self,public,transPwd):
        """
        验证交易密码
        :param public:
        :return:
        """
        self.params = {
            "transPwd":transPwd
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if transPwd != '1545154':
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'
        elif transPwd == '1545154':
            assert '交易密码错误' in self.result['msg']
            assert self.result['result'] == '12000'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))