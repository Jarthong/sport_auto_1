#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_TransPwd_Modify(object):
    """修改交易密码"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/wallet/transPwd/validate"
        self.headers = login_match[-1]

    transPwd = [Encrypt().md5Encode("905987"),'123456',None]
    oldTransPwd = [Encrypt().md5Encode("905987")]
    @pytest.mark.parametrize('transPwd',transPwd)
    @pytest.mark.parametrize('oldTransPwd',oldTransPwd)
    def test_transpwd_modify(self,public,oldTransPwd,transPwd):
        """
        修改交易密码
        :param public:
        :return:
        """
        self.params = {
            "oldTransPwd":oldTransPwd,
            "transPwd":transPwd
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['transPwd'] != '123456' and self.params['transPwd'] is not None :
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'
        elif self.params['transPwd'] == '123456':
            assert '交易密码错误' in self.result['msg']
        elif self.params['transPwd'] is None:
            assert '参数错误' in self.result['msg']

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

