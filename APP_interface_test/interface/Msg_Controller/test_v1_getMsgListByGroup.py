#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Msg_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_GetMsgListByGroup(object):
    """根据消息分类获取消息列表"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/msg/getMsgListByGroup"
        self.headers = login_match[-1]

    msgType = [Msg_Controller().msg_info(),None]
    @pytest.mark.parametrize('msgType',msgType)
    def test_getmslistbygroup(self,public,msgType):
        """
        根据消息分类获取消息列表
        :param public:
        :return:
        """
        self.params = {
            "msgType":msgType,
            "pageNo":1,
            "pageSize":15,
            "lang":'zh_CN'
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['msgType'] is not None:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['msgType'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

















