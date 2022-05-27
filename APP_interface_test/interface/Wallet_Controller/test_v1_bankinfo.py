#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os

from db_fixture.common import RandomVar
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Wallet_Controller.data_fixture import Wallet_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_BankInfo(object):
    """获取银行信息"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/wallet/bankInfo"
        self.headers = login_match[-1]

    cardNo = [(Wallet_Controller().pay_card_bin()+ '75524%s' % RandomVar().random_num()),None,47362433824]
    @pytest.mark.parametrize('cardNo',cardNo)
    def test_bankinfo(self,public,cardNo):
        """
        获取银行信息
        :param public:
        :return:
        """
        self.params = {
            "cardNo":cardNo
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['cardNo'] is not None and self.params['cardNo'] != 47362433824:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['cardNo'] is None:
            assert '参数错误' in self.result['msg']
        elif self.params['cardNo'] != 47362433824:
            assert self.params['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
















