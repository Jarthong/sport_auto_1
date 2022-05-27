#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_Upload_Cate(object):
    """获取用户上传视频分类名称功能接口"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/video/uploadCate"
        self.headers = login_match[-1]

    userId = [GlobalVar().USERIDS[0],'^&*^7',None]
    @pytest.mark.parametrize('userId',userId)
    def test_upload_cate(self,public,userId):
        """
        获取用户上传视频分类名称功能接口
        :param public:
        :return:
        """
        self.params = {}
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))







