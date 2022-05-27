#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class Test_Refund_Create(object):
    """创建退款申请"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/refund/create"
        self.headers = login_match[-1]

    def test_refund_create(self,public):
        """
        创建退款申请
        :param public:
        :return:
        """
        self.params = {
            "orderNumber":'25496200426815488',
            "skuCode":'V142184433254924288021870152928460800_20180115143144_2866_20180115143144_3952',
            "refundReasonCode":'000002'
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        # assert '成功' in self.result['msg']
        # assert self.result['result'] == '0'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))





















