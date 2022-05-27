#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Match_Controller.data_fixture import *
from interface.Community_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_getGoodsOrderList(object):
    """获取订单列表"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/getGoodsOrderList"
        self.headers = login_match[-1]

    status = [1,2,3,4,5,6,7,8,9]  # 状态 1: 待支付，2: 已支付，3: 支付失败，4: 已完成，5: 已关闭，6: 退款中，7: 已退货，9：预下单成功，10：已取消
    @pytest.mark.parametrize('status',status)
    def test_getGoodsOrderList(self,public,status):
        """
        获取订单列表
        :param public:
        :return:
        """
        self.params = {
            "status":status,
            "page":1,
            "rows":15
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['status'] is not None:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


