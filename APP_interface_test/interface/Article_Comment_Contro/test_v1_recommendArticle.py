#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_Recommend_Article(object):
    """获取资讯分类列表"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/article/recommendArticle"
        self.headers = login_train[-1]

    cateId = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, None, '^&*']
    @pytest.mark.parametrize('cateId',cateId)
    def test_recommend_article(self,public,cateId):
        """
        获取资讯分类列表
        :param public:
        :return:
        """
        self.params = {
            "cateId": cateId,
            "lang": 'zh_CN',
            "pageSize":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['cateId'] is not None and self.params['cateId'] != '^&*':
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'
        elif self.params['cateId'] is None:
            assert '参数错误' in self.result['msg']
            assert self.result['result'] == '4002'
        elif self.params['cateId'] == '^&*':
            assert '参数类型错误' in self.result['msg']
            assert self.result['result'] == '4002'


