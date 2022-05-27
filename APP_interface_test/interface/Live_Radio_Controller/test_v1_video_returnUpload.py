#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

from interface.Live_Radio_Controller.test_v1_vedio_fileblock import *

urllib3.disable_warnings(InsecureRequestWarning)

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class Test_Return_Upload(object):
    """获取用户上传视频分类名称功能接口"""

    def test_return_upload(self, login_match):
        """
        获取用户上传视频分类名称功能接口
        :param public:
        :return:
        """
        self.base_url = login_match[0] + "/v1/user/video/returnUpload"
        self.headers = login_match[-1]
        self.second_url = login_match[0] + "/v1/user/video/fileBlock"
        a = requests.post(self.second_url, headers=self.headers, verify=False, params={"fileSize": "31142707"})
        self.result2 = a.json()
        t = str(self.result2['data']['hashCode'])
        self.params = {
            "fileSize": "31142707",
            "blockSize": "20971520",
            "blockNumber": "2",
            "blockIndex": "1",
            "hashCode": t
        }
        file = {'file': open(parentdir + r'\Live_Radio_Controller\video\VID_20180109_165055.mp4', 'rb')}
        u = requests.post(self.base_url, headers=self.headers, verify=False, params=self.params, files=file)
        self.result = u.json()
        print(self.result)
        # assert self.result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
