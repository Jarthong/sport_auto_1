#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
import requests

from db_fixture.common import GlobalVar
from interface.Social_Circle_Controller.data_fixture import Social_Controller


class Test_SocialCircle_Guest_Feed(object):
    """根据圈子ID获取圈子下的帖子"""

    @pytest.fixture()
    def public(self, login_hq2):
        self.base_url = login_hq2.host + "/v1/socialCircle/_guest/feed"
        self.headers = login_hq2.headers


    id = [Social_Controller().social_circle(GlobalVar().GVar_hq['user_id2']),None,'$#%']
    type = [1,2,3]
    @pytest.mark.parametrize('id',id)
    @pytest.mark.parametrize('type',type)
    def test_guest_feed(self,public,id,type):
        """
        根据圈子ID获取圈子下的帖子
        :param public:
        :return:
        """
        self.params = {
            "circleId":id,
            "type":type,
            "page":1,
            "rows":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['circleId'] is not None and self.params['circleId'] != '$#%':
            assert self.result['msg'] == '成功'
        elif self.params['circleId'] is None:
            assert '参数错误' in self.result['msg']
        elif self.params['circleId'] == '$#%':
            assert '参数类型错误' in self.result['msg']



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

    #该账号没数据导致用例失败


