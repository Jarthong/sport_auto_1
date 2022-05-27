#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os,sys
from db_fixture.login_token import *
from interface.Community_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)


class Test_PostUserFeed(object):
    """社区发贴"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/user/feed"
        self.headers = login_train[-1]


    def test_postuserfeed1(self,public):
        """
        社区发贴-文本
        :param public:
        :return:
        """
        self.params = {
            "circleId":'18485',
            "feedContents[0].content":'autotest生活如此美妙%s，好好珍惜时光'% RandomVar().random_az(),
            "feedContents[0].contentType":1,
            "feedContents[0].sortNum":"1",
            "title":'autotest%s欢迎大家来讨论'% RandomVar().random_char_upper(),
            "label":'Tag000013'
        }
        r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'
        assert self.result['result'] == '0'

    def test_postuserfeed2(self,public):
        """
        社区发帖-图片
        :param public:
        :return:
        """
        self.params = {
            "circleId":'18485',
            "feedContents[0].content":"",
            "feedContents[1].content": 'autotest生活如此美妙%s，好好珍惜时光' % RandomVar().random_az(),
            "feedContents[0].contentType":2,
            "feedContents[1].contentType":1,
            "feedContents[0].sortNum":"1",
            "feedContents[1].sortNum": "2",
            "feedContents[1].fileSize":'2081871',
            "feedContents[1].playTime":"00:15",
            "title":'autotest%s视频帖子欢迎大家来讨论'% RandomVar().random_char_upper(),
            "label":'2'
        }
        files1={'file':open(parentdir + '\\Community_Controller\\picture\\0.jpg','rb')}
        r = requests.post(self.base_url,headers=self.headers,verify=False,params=self.params,files=files1)
        self.result = r.json()
        print(self.result)
        assert self.result['msg'] == '成功'
        assert self.result['result'] == '0'

    #def test_postuserfeed3(self,public):
    #    """
    #    社区发帖-视频
    #    :param public:
    #    :return:
    #    """
    #    self.params = {
    #        "circleId":'18485',
    #        "feedContents[0].content":'autotest生活如此美妙%s，好好珍惜时光'% RandomVar().random_az(),
    #        "feedContents[0].contentType":1,
    #        "feedContents[1].contentType":3,
    #        "feedContents[0].sortNum":"1",
    #        "feedContents[1].sortNum": "2",
    #        "feedContents[1].fileSize":'2081871',
    #        "feedContents[1].playTime":"00:30",
    #        "title":'autotest%s视频帖子欢迎大家来讨论'% RandomVar().random_char_upper(),
    #        "label":'0'
    #    }
    #    files1={'file':open(parentdir + '\\Community_Controller\\video\VID_20180109_165055.mp4','rb')}
    #    r = requests.post(self.base_url,headers=self.headers,verify=False,params=self.params,files=files1)
    #    self.result = r.json()
    #    print(self.result)
    #    assert self.result['msg'] == '成功'
    #    assert self.result['result'] == '0'


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))



