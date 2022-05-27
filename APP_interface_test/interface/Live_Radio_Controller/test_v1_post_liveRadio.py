#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Live_Radio_Controller.data_fixture import Live_Radio

urllib3.disable_warnings(InsecureRequestWarning)


class Test_Live_Radio(object):
    """结束直播上报"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/liveRadio"
        self.headers = login_match[-1]

    liveId = [Live_Radio().live_radio('seedp10'),11445]
    @pytest.mark.parametrize('liveId',liveId)
    def test_live_radio(self,public,liveId):
        """
        结束直播上报
        :param public:
        :return:
        """
        self.params = {
            "liveId":liveId
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['liveId'] != 11445:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['liveId'] == 11445:
            assert '对照接口文档' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))








