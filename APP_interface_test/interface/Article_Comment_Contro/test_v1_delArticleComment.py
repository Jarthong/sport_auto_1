#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import pytest
import urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Article_Comment_Contro.data_fixture import *

urllib3.disable_warnings(InsecureRequestWarning)


class Test_DelArticleComment(object):
    """删除资讯评论信息"""

    @pytest.fixture()
    def public(self, login_train):
        self.base_url = login_train[0] + "/v1/user/article/comment/delArticleComment"
        self.headers = login_train[-1]

    commentId = [Article_Information().article_comment(), None]

    @pytest.mark.parametrize('commentId', commentId)
    def test_DelArticleComment(self, public, commentId):
        """
        删除资讯评论信息
        :param public:
        :return:
        """
        self.params = {
            "commentId": commentId
        }
        r = requests.delete(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['commentId'] is not None:
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'
        elif self.params['commentId'] is None:
            assert self.result['result'] == '4002'
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
