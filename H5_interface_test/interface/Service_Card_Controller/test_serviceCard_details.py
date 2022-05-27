#!/user/bin/python
# encoding:utf-8
# __auth__=='__hq__'

import os

import pytest
import requests
from db_fixture.common import GlobalVar

from db_fixture.getdata import GetData


@pytest.mark.parametrize('cardNo', [
    GetData(column='card_no', table='service_card', where="where consumer_id='seedp546981'").result(),
    None,
    '%^&*'])
@pytest.mark.parametrize('consumerId', [GlobalVar().GVar['user_id']])
def test_servicecard_details(login_hq, cardNo, consumerId):
    """
    获取服务卡列表
    busType:
    业务类型：0通用购买、1赛事、2培训、3票务
    state:
    1未激活 3已完成 5已终止
    :param public:
    :return:
    """
    base_url = login_hq.host + "/v1/user/serviceCard/details"
    params = {
        "cardNo": cardNo,
        "providerId": None,
        "consumerId": consumerId,
        "deviceType": 4
    }
    r = requests.get(base_url, headers=login_hq.headers, verify=False, params=params)
    result = r.json()
    print(result)
    if params['cardNo'] != None and params['cardNo'] != '%^&*':
        assert result['data']['cardNo'] == cardNo
        print(cardNo)


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
