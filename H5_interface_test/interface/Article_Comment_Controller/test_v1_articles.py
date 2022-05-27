#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os

import pytest
import requests


class Test_Articles(object):
    """获取对应栏目分类下咨询信息列表功能接口"""

    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/article/articles"
        self.headers = login.headers

    categoryId = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, None]

    @pytest.mark.parametrize('categoryId', categoryId)
    def test_articles(self, public, categoryId):
        """
        获取对应栏目分类下咨询信息列表功能接口
        :param public:
        :return:
        """
        self.params = {
            "categoryId": categoryId,
            "page": 1,
            "rows": 10
        }
        r = requests.get(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['categoryId'] is not None:
            assert self.result['msg'] == '成功'
        elif self.params['categoryId'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))


