from db_fixture.getdata import GetData

__author__ = 'huxm855'
import os

import pytest
import requests

parend_Id = GetData('parent_id', 'dict_area').result()


@pytest.mark.parametrize('parentId', [parend_Id, None])
def test_dict_getareabyparentid(login, parentId):
    ''' 根据区域ID获取当前节点下区域列表'''
    base_url = login.host + "/dict/getAreaByParentId"
    params = {'parentId': parentId}
    r = requests.get(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)

    if parentId is not None:
        assert result['msg'] == '成功'
        json_values = [(data['areaId'], data['title'], data['sortValue']) for data in result['data']]
        sql_values = GetData(
            sql='SELECT area_id,title,sort_value FROM dict_area  where parent_id={parent_id}'.format(
                parent_id=parentId)).result_original()
        assert not set(json_values).difference(sql_values)#从json中获取到的值与mysql中值进行比较是否相等
    else:
        assert result['msg'] == '参数错误[Long@parentId]'


if __name__ == '__main__':
    os.system('pytest -s -vv {file}'.format(file=__file__))
