#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest
from db_fixture.login_token import *
from interface.Article_Comment_Contro.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_FindArticleComment(object):
    """获取资讯评论信息"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/article/comment/findArticleComment"
        self.headers = login_train[-1]

    articleId = [Article_Information().article(1),None]
    @pytest.mark.parametrize('articleId', articleId)
    def test_findArticleComment(self,public,articleId):
        """
        获取资讯评论信息
        :param public:
        :return:
        """
        self.params = {
            "articleId": articleId,
            "page":1,
            "rows":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['articleId'] is not None:
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'
        elif self.params['articleId'] is None:
            assert self.result['result'] == '4002'
            assert '参数错误' in self.result['msg']

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))