from db_fixture.getdata import GetData

__author__ = 'huxm855'
import os

import requests


def test_dict_company_type(login):
    ''' 公司类型基础数据查询，DICT_TYPE=31'''
    base_url = login.host + "/dict/company/type"
    r = requests.get(base_url, headers=login.headers, verify=False)
    result = r.json()
    print(result)
    assert result['msg'] == '成功'
    assert not set([(data['id'], data['title']) for data in result['data']['dicts']]).difference(set(GetData(
        sql='select field_value,field_name from dict_common  where version=0 and dict_type=31').result_original()))


if __name__ == '__main__':
    os.system('pytest -s -vv {file}'.format(file=__file__))
    pass
