#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Search_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_SearchGoods(object):
    """搜索商品"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/search/goods"
        self.headers = login_match[-1]

    keyword = [Search_Controller().goods_category()[1],None]
    @pytest.mark.parametrize('keyword',keyword)
    def test_searchgoods(self,public,keyword):
        """
        搜索商品
        :param public:
        :return:
        """
        self.params = {
            "keyword":keyword,
            "cateCode":'',
            "page":1,
            "rows":15
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['keyword'] is not None:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['keyword'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))















