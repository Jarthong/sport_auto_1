from db_fixture.getdata import GetData

__author__ = 'huxm855'
import os
import pytest
import requests

parentValue, dictType = GetData('parent_value, dict_type', 'dict_common').result()
parentValues = [parentValue, None]
dictTypes = [dictType, None]


@pytest.mark.parametrize('parentValues', parentValues)
@pytest.mark.parametrize('dictTypes', dictTypes)
def test_dict_getbyparentandtype(login, parentValues, dictTypes):
    ''' 获取字典子节点下面的数据'''
    base_url = login.host + "/dict/getByParentAndType"
    params = {'parentValue': parentValues, 'dictType': dictTypes}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    if parentValues is None:
        assert result['msg'] == '参数错误[Integer@parentValue]'
    elif dictTypes is None:
        assert result['msg'] == '参数错误[Integer@dictType]'
    else:
        assert result['msg'] == '成功'
        json_values = [(data['fieldName'], data['fieldValue'], data['dictType'], data['parentValue']) for data in
                       result['data']]
        sql_values = GetData(
            sql='select field_name,field_value,dict_type,parent_value from dict_common  where dict_type={dictType} and parent_Value={parentValue}'.format(
                **params)).result_original()
        assert not set(json_values).difference(sql_values)  # 从json中获取到的值与mysql中值进行比较是否相等


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
