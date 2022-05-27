__author__ = 'huxm855'
import os

import pytest
import requests

from db_fixture.common import GlobalVar

type = list(range(1, 5)) + [None]


@pytest.mark.parametrize('type', type)
def test_generateImgValidateCode(type):
    ''' 获取图片验证码 1:登录;2:注册;3:激活;4:绑定手机;5:激活验证;6:忘记密码'''
    base_url = GlobalVar.GVar['host'] + "/guest/generateImgValidateCode"
    params = {"width": "116", "height": "36", 'type': type}
    r = requests.get(base_url, params=params, verify=False)
    result = r.json()
    print(result)
    if params['type'] is None:
        assert result['result'] == '4002'
        assert result['msg'] == '参数错误[Integer@type]'
    else:
        assert result['msg'] == '成功'
        assert result['data']['image'] is not None
        assert result['data']['key'] is not None


if __name__ == '__main__':
    os.system('pytest -s -v test_guest_generateImgValidateCode.py')
