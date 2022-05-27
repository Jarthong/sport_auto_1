#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from  db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Article_Comment_Controller.data_fixture import Article_Information

urllib3.disable_warnings(InsecureRequestWarning)


class Test_Article_Other(object):
    """获取资讯组图的所有信息详情功能接口"""

    @pytest.fixture()
    def public(self,login):
        self.base_url = login.host + "/v1/article/article/acticleOther"
        self.headers = login.headers

    articleId = [Article_Information().article(0)[0],Article_Information().article(1)[0],None]
    @pytest.mark.parametrize('articleId',articleId)
    def test_article_other(self,public,articleId):
        """
        获取资讯组图的所有信息详情功能接口
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
        elif self.params['articleId'] is None:
            assert '参数错误' in self.result['msg']



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



