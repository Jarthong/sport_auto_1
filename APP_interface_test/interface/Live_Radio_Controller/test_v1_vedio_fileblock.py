#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os,sys
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

class Test_File_Block(object):
    """视频分块续传分块功能接口"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/user/video/fileBlock"
        self.headers = login_match[-1]


    def test1_file_block(self,public):
        """
        视频分块续传分块功能接口
        :param public:
        :return:
        """
        self.params = {
            "fileSize":"31142707"
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'
        return self.result['data']['hashCode']

    # hashCode = ['0C6A9C777D74495B9C36DE70CB76C6AE']
    # @pytest.mark.parametrize('hashCode',hashCode)
    # def test2_return_upload(self,public,hashCode):
    #     """
    #     获取用户上传视频分类名称功能接口
    #     :param public:
    #     :return:
    #     """
    #     self.params = {
    #         "fileSize":"31142707",
    #         "blockSize":"20971520",
    #         "blockNumber":"2",
    #         "blockIndex":"1",
    #         "hashCode":hashCode
    #     }
    #     file = {'file':open(parentdir + r'\Live_Radio_Controller\video\VID_20180109_165055.mp4','rb')}
    #     r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params,files=file)
    #     self.result = r.json()
    #     print(self.result)
    #     assert self.result['result'] == '0'
    #     assert self.result['msg'] == '成功'




if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))








