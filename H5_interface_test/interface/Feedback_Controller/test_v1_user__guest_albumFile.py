from db_fixture.common import GlobalVar

__author__ = 'huxm855'

import os

import pytest
import requests

# 资源类型：2,图片;3,视频
resType = [2, 3]
# 资源文件用途：1,用户相册图；2,IP推荐图；3,用户上传视频;4,直播直播封面;5,举报图片;6,直播回放封面;7,组织logo
purType = list(range(1, 8))


@pytest.mark.parametrize('rows', [10, 20, 50, 100])
@pytest.mark.parametrize('userId', ['None', GlobalVar.GVar['user_id'], 'hhly'])
@pytest.mark.parametrize('resType', resType)
@pytest.mark.parametrize('purType', purType)
def test_v1_user__guest_albumFile(login, resType, purType, rows, userId):
    ''' 个人中心查看用户相册和视频功能接口'''
    base_url = login.host + "/v1/user/_guest/albumFile"
    params = {'userId': userId, 'resType': resType, 'purType': purType, 'page': 1, 'rows': rows}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert result['data']['total'] >= 0
    if result['data']['total'] > 0:
        assert result['data']['rows'] == rows


if __name__ == '__main__':
    os.system('pytest -s -v -x {file}'.format(file=__file__))
