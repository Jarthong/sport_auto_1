from db_fixture.getdata import GetData

__author__ = 'huxm855'
import os

import pytest
import requests

dictType = GetData(sql='select distinct(dict_type) from dict_other').results()
print(dictType)


@pytest.mark.parametrize('dictType', [dictType, None])
def test_dict_getbydicttype(login, dictType):
    ''' 获取字典信息'''
    base_url = login.host + "/dict/getByDictType"
    params = {'dictType': dictType}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    if dictType is None:
        assert result['msg'] == '参数错误[Integer@dictType]'
    else:
        if isinstance(dictType, (tuple, list)):
            dictType = dictType[0]
        else:
            dictType = dictType
        assert result['msg'] == '成功'
        json_values = [(data['id'], data['dictType'], data['fieldName']) for data in result['data']]
        sql_values = GetData(
            sql='SELECT id,dict_Type,field_Name from dict_other  where dict_type={dictType}'.format(
                dictType=dictType)).result_original()
        assert not set(json_values).difference(sql_values)  # 从json中获取到的值与mysql中值进行比较是否相等


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
