#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os

from db_fixture.common import RandomVar
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_Live_Radio(object):
    """申请直播"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/liveRadio"
        self.headers = login_match[-1]

    cateId = [1]
    @pytest.mark.parametrize('cateId',cateId)
    def test_live_radio(self,public,cateId):
        """
        申请直播
        :param public:
        :return:
        """
        self.params = {
            "cateId":cateId,
            "liveTitle":'autotest%s的直播'% RandomVar().random_az(),
            "fileId":45114,
            "osType":'',
            "longitude":"113.947426",
            "latitude":"22.544619"
        }
        r = requests.put(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))








