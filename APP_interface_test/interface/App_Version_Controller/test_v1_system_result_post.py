__author__ = 'huxm855'
import os

import pytest
import requests


@pytest.mark.parametrize('result', range(0, 100))
def test_v1_system_result(login, result):
    ''' 输出 SNSResult'''
    base_url = login[0] + "/v1/system/result"
    params = {'result': result}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    results = r.json()
    print(results)
    assert results['result'] == str(result)


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
