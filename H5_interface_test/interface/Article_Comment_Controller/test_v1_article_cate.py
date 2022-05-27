#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
import requests


class Test_Article_Cate(object):
    """获取资讯栏目分类列表功能接口"""

    @pytest.fixture()
    def public(self,login):
        self.base_url = login.host + "/v1/article/cate"
        self.headers = login.headers


    def test_article_cate(self,public):
        """
        获取资讯栏目分类列表功能接口
        :param public:
        :return:
        """
        r = requests.get(self.base_url,headers = self.headers,verify=False)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'




if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))




