#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_availableList(object):
    """可用优惠券列表"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/coupon/availableList"
        self.headers = login_match[-1]

    totalAmount = [100,None]
    @pytest.mark.parametrize('totalAmount',totalAmount)
    def test_availablelist(self,public,totalAmount):
        """
        可用优惠券列表
        :param public:
        :return:
        """
        self.params = {
            "totalAmount":totalAmount,
            "page":1,
            "rows":15
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['totalAmount'] == 100:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['totalAmount'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



