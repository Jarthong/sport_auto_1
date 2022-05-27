#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Guest_Controller.data_fixture import Guest_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_ChannelContentList(object):
    """获取频道内容列表"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/guest/channelContentList"
        self.headers = login_match[-1]

    espnCode = [Guest_Controller().espn(),None]
    @pytest.mark.parametrize('espnCode',espnCode)
    def test_channelContentlist(self,public,espnCode):
        """
        获取频道内容列表
        :param public:
        :return:
        """
        self.params = {
            "espnCode":espnCode,
            "page": 1,
            "rows":15
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['espnCode'] is not None:
            assert self.result['msg'] == '成功'
        elif self.params['espnCode'] is None:
            assert '成功' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))









