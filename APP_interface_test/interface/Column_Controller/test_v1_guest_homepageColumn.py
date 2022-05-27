# -*- coding: utf-8 -*-
from interface.Column_Controller.data_fixture import Column_Controller

__author__ = 'huxm855'
import os

import requests


def test_v1_guest_homepageColumn(login):
    """"获取app首页展示栏目"""

    base_url = login[0] + "/v1/guest/homepageColumn"
    r = requests.get(base_url, headers=login[-1], verify=False)
    result = r.json()
    assert result['msg'] == '成功'
    for datas in result['data']:
        assert datas['columnTitle'] in [columnTitle[0] for columnTitle in
                                        Column_Controller().homepage_column()]  # 返回参数columnTitle 在首页栏目表中有找到


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
