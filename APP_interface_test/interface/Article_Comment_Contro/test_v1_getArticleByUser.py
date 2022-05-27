#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'
import os

import pytest
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Article_Comment_Contro.data_fixture import Article_Information

urllib3.disable_warnings(InsecureRequestWarning)


class Test_GetArticleByUser(object):
    """根据用户获取资讯列表"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/article/getArticleByUser"
        self.headers = login_train[-1]

    userId = [Article_Information().article(1)[1],None]
    @pytest.mark.parametrize('userId',userId)
    def test_getarticlebyuser(self,public,userId):
        """
        根据用户获取资讯列表
        :param public:
        :return:
        """
        self.params = {
            "userId": userId,
            "lang": 'zh_CN',
            "pageNO":1,
            "pageSize":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['userId'] is not None:
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
