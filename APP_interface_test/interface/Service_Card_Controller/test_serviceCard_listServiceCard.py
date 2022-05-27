#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from  db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_Service_ListServiceCard(object):
    """获取服务卡列表"""

    @pytest.fixture()
    def public(self,login_2):
        self.base_url = login_2[0] + "/v1/serviceCard/listServiceCard"
        self.headers = login_2[-1]

    busType = [0]
    state = [1,3,5,'$%^']
    @pytest.mark.parametrize('state',state)
    @pytest.mark.parametrize('busType',busType)
    def test_service_listservicecard(self,public,busType,state):
        """
        获取服务卡列表
        busType:
        业务类型：0通用购买、1赛事、2培训、3票务
        state:
        1未激活 3已完成 5已终止
        :param public:
        :return:
        """
        self.params = {
            "busType":busType,
            "state": state,
            "page":1,
            "rows":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['state'] == '$%^':
            assert '参数类型错误' in self.result['msg']
        elif self.params['state'] != '$%^':
            assert '成功' in self.result['msg']



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))




