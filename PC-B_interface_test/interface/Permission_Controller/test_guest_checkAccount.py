__author__ = 'huxm855'
import os

import pytest
import requests

from db_fixture.common import GlobalVar

account = [GlobalVar.GVar['user_phone'], "1888", "100htxk@13322.com", "1888@qq.com"]
remarks = ['True', 'False', 'True', 'False']


@pytest.mark.parametrize('account,data', list(zip(account, remarks)), ids=remarks)
def test_checkAccount(account, data):
    ''' 检查账号测试 '''
    params = {"account": account}
    base_url = GlobalVar.GVar['host'] + "/guest/checkAccount"
    r = requests.get(base_url, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert str(result['data']) == data


if __name__ == '__main__':
    os.system('pytest -s -v test_guest_checkAccount.py')
