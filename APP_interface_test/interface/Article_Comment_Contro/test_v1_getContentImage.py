#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Article_Comment_Contro.data_fixture import Article_Information

urllib3.disable_warnings(InsecureRequestWarning)


class Test_GetContentImage(object):
    """获取资讯分类列表"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/article/getContentImage"
        self.headers = login_train[-1]

    articleId = [Article_Information().article(1)[0], None]
    @pytest.mark.parametrize('articleId',articleId)
    def test_getcontentimage(self,public,articleId):
        """
        获取资讯分类列表
        :param public:
        :return:
        """
        self.params = {
            "articleId": articleId,
            "lang": 'zh_CN',
            "pageNO":1,
            "pageSize":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['articleId'] is not None:
            assert self.result['msg'] == '成功'
            assert self.result['result'] == '0'
        elif self.params['articleId'] is None:
            assert '参数错误' in self.result['msg']
            assert self.result['result'] == '4002'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
