#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Msg_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_MsgOperating(object):
    """消息处理接口"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/msg/msgOperating"
        self.headers = login_match[-1]

    id = [Msg_Controller().msg_info1005(1005)]
    msgStatus = [2,3,4,5,6]
    @pytest.mark.parametrize('id',id)
    @pytest.mark.parametrize('msgStatus',msgStatus)
    def test_MsgOperating(self,public,id,msgStatus):
        """
        消息处理接口
        :param public:
        :return:
        """
        self.params = {
            "id":id,
            "msgStatus":msgStatus
        }
        print(self.params)
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

















