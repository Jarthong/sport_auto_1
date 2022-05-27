#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_TransPwd_Set(object):
    """设置/忘记交易密码"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/wallet/transPwd/validate"
        self.second_url = login_match[0] + "/v1/user/validateSmsCodeForBindedPhone"
        self.third_url = login_match[0] + "/v1/user/sendSmsCodeToBindedPhone"
        self.headers = login_match[-1]

    transPwd = [Encrypt().md5Encode("905987")]
    @pytest.mark.parametrize('transPwd',transPwd)
    def test_transpwd_set(self,public,transPwd):
        """
        设置/忘记交易密码，操作类型:8设置交易密码，9忘记交易密码
        :param public:
        :return:
        """
        a = requests.get(self.third_url,headers = self.headers,verify=False,params={
            "operateType":9
        })
        self.result3 = a.json()
        time.sleep(3)
        print(self.result3)
        b = requests.get(self.second_url,headers = self.headers,verify=False,params={
            "smsCode":666666,
            "operateType":9
        })
        self.result2 = b.json()
        time.sleep(3)
        print(self.result2)
        self.params = {
            "transPwd":transPwd,
            "smsCode":666666,
            "opterType":9
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'
        assert self.result['result'] == '0'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
