#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os
import pytest
import requests

from interface.Article_Comment_Controller.data_fixture import Article_Information


class Test_Recomment_Article(object):
    """推荐资讯组图"""

    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/article/article/recommendArticle"
        self.headers = login.headers

    articleId = [Article_Information().article(0)[0], Article_Information().article(1)[0], None]
    cateId = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    @pytest.mark.parametrize('articleId', articleId)
    @pytest.mark.parametrize('cateId', cateId)
    def test_recomment_article(self, public, articleId, cateId):
        """
        推荐资讯组图
        :param public:
        :return:
        """
        self.params = {
            "articleId": articleId,
            "cateId": cateId,
            "page": 1,
            "rows": 10
        }
        r = requests.get(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['articleId'] is not None:
            assert self.result['msg'] == '成功'
        elif self.params['articleId'] is None:
            assert '成功' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
