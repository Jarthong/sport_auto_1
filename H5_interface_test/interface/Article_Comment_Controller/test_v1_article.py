#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'
import os

import pytest
import requests

from interface.Article_Comment_Controller.data_fixture import Article_Information


class Test_Article(object):
    """获取资讯文章详细信息功能接口"""

    @pytest.fixture()
    def public(self,login):
        self.base_url = login.host + "/v1/article/article"
        self.headers = login.headers

    articleId = [Article_Information().article(0)[0],Article_Information().article(1)[0],None]
    @pytest.mark.parametrize('articleId',articleId)
    def test_article(self,public,articleId):
        """
        获取资讯文章详细信息功能接口
        :param public:
        :return:
        """
        self.params = {
            "articleId": articleId
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['articleId'] is not None:
            assert self.result['msg'] == '成功'
        elif self.params['articleId'] is None:
            assert '参数错误' in self.result['msg']



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

