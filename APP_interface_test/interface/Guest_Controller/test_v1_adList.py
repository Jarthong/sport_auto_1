#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_AdList(object):
    """获取广告列表"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/guest/adList"
        self.headers = login_match[-1]

    showPosition = [21,22,23,25]
    adsType = ['banner','screen','startPage']
    @pytest.mark.parametrize('adsType',adsType)
    @pytest.mark.parametrize('showPosition',showPosition)
    def test_adlist(self,public,adsType,showPosition):
        """
        获取广告列表
        :param public:
        :return:
        """
        self.params = {
            "channelNO":"com.qiumiao1",
            "adsType": adsType,
            "showPosition":showPosition
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['showPosition'] == 21 and self.params['adsType'] == 'banner':
            assert self.result['msg'] == '成功'
        elif self.params['showPosition'] ==25 and self.params['adsType'] == 'banner':
            assert self.result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))








