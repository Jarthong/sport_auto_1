#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'
import os

import pytest
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_GetArticleByCateGory(object):
    """根据分类获取资讯列表"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/article/getArticleByCategory"
        self.headers = login_train[-1]

    categoryId = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,None,'^&*']
    @pytest.mark.parametrize('categoryId',categoryId)
    def test_getarticlebycategory(self,public,categoryId):
        """
        根据分类获取资讯列表
        :param public:
        :return:
        """
        self.params = {
            "categoryId": categoryId,
            "lang": 'zh_CN',
            "pageNO":1,
            "pageSize":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['categoryId'] is not None and self.params['categoryId'] != '^&*':
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'
        elif self.params['categoryId'] == '^&*':
            assert self.result['result'] == '4002'
            assert '参数类型错误' in self.result['msg']
        elif self.params['categoryId'] is None:
            assert self.result['result'] == '2'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
