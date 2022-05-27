__author__ = 'huxm855'
import os
import requests


def test_v1_system_resultList(login):
    ''' 输出所有错误码和对应的错误消息'''
    base_url =login[0] + "/v1/system/resultList"
    r = requests.get(base_url, headers=login[-1], verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    
if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))