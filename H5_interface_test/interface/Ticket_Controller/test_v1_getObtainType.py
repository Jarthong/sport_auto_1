#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'
import os

import pytest
import requests


class Test_GetObtainType(object):
    """获取票务支持的取票方式"""

    @pytest.fixture()
    def public(self, login):
        self.base_url = login.host + "/v1/ticket/getObtainType"
        self.headers = login.headers

    goodsCode = ['V181001_20180305165932_2954', None]

    @pytest.mark.parametrize('goodsCode', goodsCode)
    def test_getobtaintype(self, public, goodsCode):
        """
        获取票务支持的取票方式
        :param public:
        :return:
        """
        self.params = {
            "goodsCode": goodsCode
        }
        r = requests.get(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['goodsCode'] is not None:
            assert self.result['msg'] == '成功'
        elif self.params['goodsCode'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
#断言失败