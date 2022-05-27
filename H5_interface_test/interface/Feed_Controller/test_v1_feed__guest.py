__author__ = 'huxm855'
import pytest
import requests


def test_v1_feed__guest(login):
    ''' 未登录时首页展示所有微博动态功能接口'''
    base_url = login.host + "/v1/feed/_guest"
    r = requests.get(base_url, headers=login.headers, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert len(result['data']) > 0


if __name__ == '__main__':
    pytest.main(['-s','-v',__file__])