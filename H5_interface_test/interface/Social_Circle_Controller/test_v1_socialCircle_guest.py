#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'
import os

import pytest
import requests

from db_fixture.common import GlobalVar
from interface.Social_Circle_Controller.data_fixture import Social_Controller


id = [Social_Controller().social_circle(GlobalVar().GVar_hq['user_id2']), None, '$%^%$$']

@pytest.mark.parametrize('id', id)
def test_guest(login_hq2, id):
    """
    根据ID查询圈子
    :param public:
    :return:
    """
    base_url = login_hq2.host + "/v1/socialCircle/_guest"
    headers = login_hq2.headers
    params = {
        "id": id
    }
    r = requests.get(base_url, headers=headers, verify=False, params=params)
    result = r.json()
    print(result)
    if params['id'] is not None and params['id'] != '$%^%$$':
        assert result['msg'] == '成功'
    elif params['id'] is None:
        assert '参数错误' in result['msg']
    elif params['id'] == '$%^%$$':
        assert '参数类型错误' in result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

    #该账号没数据导致用例失败
