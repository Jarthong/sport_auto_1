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


class Test_matchInfoByGoodsGode(object):
    """根据商品Code获取赛事信息"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/matchInfoByGoodsGode"
        self.headers = login_train[-1]


    goodsCode = [Match_Controller().Match(4)[1],None]
    @pytest.mark.parametrize('goodsCode',goodsCode)
    def test_matchInfoByGoodsGode(self,public,goodsCode):
        """
        根据商品Code获取赛事信息
        :param public:
        :return:
        """
        self.params = {
            "goodsCode":goodsCode
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['goodsCode'] is not None:
            assert self.result['result'] == '0'
        elif self.params['goodsCode'] is None:
            assert '参数错误' in self.result['msg']
            assert self.result['result'] == '4002'




if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))







