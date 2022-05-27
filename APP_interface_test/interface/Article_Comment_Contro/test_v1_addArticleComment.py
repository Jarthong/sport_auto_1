#!/user/bin/python
# encoding:utf-8

# __auth__=='__hq__'

import pytest
import urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Article_Comment_Contro.data_fixture import *

urllib3.disable_warnings(InsecureRequestWarning)


class Test_AddArticleComment(object):
    """新增资讯评论信息"""

    @pytest.fixture()
    def public(self, login_train):
        self.base_url = login_train[0] + "/v1/user/article/comment/addArticleComment"
        self.headers = login_train[-1]

    articleId = [Article_Information().article(1)[0], None]
    content = ['autotest%sp赛事精彩，不容错过' % RandomVar().random_az(), None]

    @pytest.mark.parametrize('articleId', articleId)
    @pytest.mark.parametrize('content', content)
    def test_AddArticleComment(self, public, articleId, content):
        """
        新增资讯评论信息
        :param public:
        :return:
        """
        self.params = {
            "articleId": articleId,
            "content": content
        }
        r = requests.post(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.params['articleId'])
        print(self.result)
        if self.params['articleId'] is not None and self.params['content'] is not None:
            assert self.result['msg'] == '成功'
        elif self.params['articleId'] is None and self.params['content'] is not None:
            assert self.result['msg'] == '资讯Id不能为空'
            assert self.result['result'] == '4002'
        elif self.params['content'] is None and self.params['articleId'] is not None:
            assert self.result['msg'] == '资讯评论内容不能为空'
            assert self.result['result'] == '4002'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
