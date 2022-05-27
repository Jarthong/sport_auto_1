__author__ = 'huxm855'

import os

import pytest
import requests

from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData


@pytest.mark.parametrize('type', range(1, 4))
def test_v1_file_image(login, type):
    ''' 获取评论图片'''
    base_url = login[0] + "/v1/file/image"

    file_id = GetData('fc.file_id',table='feed f inner join feed_comment fc on f.feed_id=fc.feed_id',
                      where="f.user_id='{userid}' and f.is_del=0 and fc.file_id !=0 ".format(
                          userid=GlobalVar.GVar_hxm['user_id'], type=type)).result()
    params = {'fileId': file_id, 'width': 100, 'height': 100}
    r = requests.get(base_url, headers=login[-1], params=params, verify=False)
    assert len(r.content) > 2000
    assert r.status_code == 200


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
