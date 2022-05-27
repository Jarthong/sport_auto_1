#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_withdrawBankCard_PreBind(object):
    """预绑定提现银行卡,此接口只验证功能，由于无法实时获取验证码，参数按写死了处理"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/wallet/withdrawBankCard/preBind"
        self.headers = login_match[-1]


    def test_withdrawbankcard_prebind(self,public):
        """
        预绑定提现银行卡
        :param public:
        :return:
        """
        self.params = {
            "platformCode":"100305",
            "devicesCode": "4340617552456851",
            "mediumCode": "200001",
            "identityCode": "440305199101019351",
            "identityName": "黄呆",
            "phone": "13026644174"
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '证件号、证件姓名与已存在的用户信息不一致'
        assert self.result['result'] == '12009'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


































