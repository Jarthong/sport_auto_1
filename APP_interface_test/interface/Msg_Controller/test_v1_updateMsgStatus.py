#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Msg_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_UpdateMsgStatus(object):
    """设置消息为已读"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/msg/updateMsgStatus"
        self.headers = login_match[-1]

    idList = [Msg_Controller().msg_user_mapping('seedp10'),None]
    @pytest.mark.parametrize('idList',idList)
    def test_updatemsgstatus(self,public,idList):
        """
        设置消息为已读
        :param public:
        :return:
        """
        self.params = {
            "idList":idList,
            "userStatus":1,
            "isDelete":1,
            "lang":'zh_CN'
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['idList'] is not None:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['idList'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


















