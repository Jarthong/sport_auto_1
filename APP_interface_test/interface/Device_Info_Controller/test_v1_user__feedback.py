# -*- coding: utf-8 -*-
__author__ = 'huxm855'

import os

import pytest
import requests

content = [None, 's', 'test' * 50, 's' * 1200]
contactWay = ['18770048010', '01454245', None]

@pytest.mark.parametrize('content', content, ids=['None', '1', '200', 'more than 200'])
@pytest.mark.parametrize('contactWay', contactWay)
def test_v1_user__feedback(login, content, contactWay):
    ''' 意见反馈'''
    base_url = login[0] + "/v1/user/_feedback"
    params = {'content': content, 'contactWay': contactWay}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if content == None or contactWay == None:
        assert result['result'] in ('1000', '4002')
    elif content == 's' * 1200:
        assert result['msg'] == '反馈内容，限200字符以内'
    else:
        assert result['msg'] == '成功'
        assert result['data'] >= 0


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
