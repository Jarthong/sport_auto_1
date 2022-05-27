#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Order_Controller.data_fixture import *
from interface.Community_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_GoodsOrderCancer_Reason(object):

    def test_goodsOrdercancel_reason(self,login_match):
        """
        取消（商品）订单原因
        :param public:
        :return:
        """
        self.headers = login_match[-1]
        self.base_url = login_match[0] + "/v1/user/goodsOrder/cancelReasons"
        self.params = {}
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


