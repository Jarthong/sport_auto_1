#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class Test_Refund_Detail(object):
    """查询退款详情"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/refund/detail"
        self.headers = login_match[-1]

    refundNumber = [25496388888428544,None]
    @pytest.mark.parametrize('refundNumber',refundNumber)
    def test_refund_detail(self,public,refundNumber):
        """
        查询退款详情
        :param public:
        :return:
        """
        self.params = {
            "refundNumber":refundNumber
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['refundNumber'] == 25496388888428544:
            assert '成功' in self.result['msg']
            assert self.result['result'] == '0'
        elif self.params['refundNumber'] == None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






















