__author__ = 'huxm855'
import os

import requests


def test_v1_system_result(login):
    ''' 输出 SNSResult'''
    base_url = login[0] + "/v1/system/result"
    params = {'result': 1001}
    r = requests.delete(base_url, headers=login[-1], params=params, verify=False)
    results = r.json()
    print(results)
    assert results['result'] == str(params['result'])


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
