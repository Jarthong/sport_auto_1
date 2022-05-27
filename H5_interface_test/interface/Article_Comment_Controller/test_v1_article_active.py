#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from  db_fixture.login_token import *



class Test_Articles_Active(object):
    """批量获取资讯文章详细信息功能接口"""

    @pytest.fixture()
    def public(self,login):
        self.base_url = login.host + "/v1/article/articlesActive"
        self.headers = login.headers


    def test_articles_active(self,public):
        """
        批量获取资讯文章详细信息功能接口
        :param public:
        :return:
        """
        r = requests.get(self.base_url,headers = self.headers,verify=False)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'




if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))





