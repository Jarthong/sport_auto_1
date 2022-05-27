__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import random

import pytest
import requests

from db_fixture.common import GlobalVar
# 上传文件
pictures=os.path.dirname(os.path.dirname((os.path.abspath(os.path.dirname(__file__)))))+'\\common\\pictures\\'+str(random.choice(range(20)))+'.jpg'
# pictures目录随机选择文件
#资源文件用途：1,用户相册图；2,IP推荐图；3,用户上传视频;4,直播直播封面;5,举报图片;6,直播回放封面;7,组织logo 8,认证相关;9,社区圈子图像
@pytest.mark.parametrize('purpose',range(1,10))
# 资源文件类型:2图片3视频
@pytest.mark.parametrize('type',list(range(2,4)))

def test_v1_user_uploadFile(login,purpose,type):
    ''' 上行资源文件'''
    base_url =login[0] + "/v1/user/uploadFile"
    files = {'file': open(pictures, 'rb')}
    params={'purpose':purpose,'type':type}
    r = requests.post(base_url, headers=login[-1], params=params,files=files,verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    assert result['data'][0]['userId'] ==GlobalVar.GVar_hxm['user_id']
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
