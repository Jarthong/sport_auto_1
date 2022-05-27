#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

from interface.Live_Radio_Controller.test_v1_vedio_fileblock import *

urllib3.disable_warnings(InsecureRequestWarning)

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class Test_delFile_Block(object):
    """视频上传中删除功能接口"""

    def test_defFile_Block(self, login_match):
        """
        视频上传中删除功能接口
        :param public:
        :return:
        """
        self.base_url = login_match[0] + "/v1/user/video/fileBlock"
        self.headers = login_match[-1]
        self.second_url = login_match[0] + "/v1/user/video/fileBlock"
        a = requests.post(self.second_url, headers=self.headers, verify=False, params={"fileSize": "31142707"})
        self.result2 = a.json()
        t = str(self.result2['data']['hashCode'])
        self.params = {
            "hashCode": t
        }
        u = requests.delete(self.base_url, headers=self.headers, verify=False, params=self.params)
        self.result = u.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert self.result['msg'] == '成功'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
