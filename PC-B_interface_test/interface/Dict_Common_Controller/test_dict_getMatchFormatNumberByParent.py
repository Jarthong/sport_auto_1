from db_fixture.getdata import GetData

__author__ = 'huxm855'
import os
import pytest
import re
import requests
#dict_type=23
parentValue=list(GetData(sql='select distinct(parent_value) from dict_common where dict_type=23 order by parent_value asc').results())+[None]
@pytest.mark.parametrize('parentValue',parentValue)
def test_dict_getmatchformatnumberbyparent(login,parentValue):
    ''' 获取赛制下面的具体赛制信息'''
    base_url =login.host + "/dict/getMatchFormatNumberByParent"
    params={'parentValue':parentValue}
    r = requests.get(base_url, headers=login.headers, params=params,verify=False)
    result = r.json()

    print(result)
    if parentValue is None:
        assert result['msg']=='参数错误[Integer@parentValue]'
    else:
        assert result['msg'] == '成功'
        json_values = [(data['dictId'], data['fieldName'], data['fieldValue'],data['dictType'],data['parentValue']) for data in result['data']]
        sql_values = GetData(
            sql='SELECT dict_Id,field_Name,field_Value,dict_Type,parent_Value from dict_common  where parent_Value={parentValue}'.format(
                parentValue=parentValue)).result_original()
        assert not set(json_values).difference(sql_values)  # 从json中获取到的值与mysql中值进行比较是否相等
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))