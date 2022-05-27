#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Community_Controller.data_fixture import Community_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_delFeed(object):
    """删除圈子下的帖子"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/circle/delFeed"
        self.headers = login_train[-1]

    feedId = [Community_Controller().feed_circle(18485)[0],999999]
    circleId = [Community_Controller().feed_circle(18485)[1]]
    @pytest.mark.parametrize('feedId',feedId)
    @pytest.mark.parametrize('circleId',circleId)
    def test_delFeed(self,public,feedId,circleId):
        """
        删除圈子下的帖子
        :param public:
        :return:
        """
        self.params = {
            "feedId":feedId,
            "circleId":circleId
        }
        r = requests.delete(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)




if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))






