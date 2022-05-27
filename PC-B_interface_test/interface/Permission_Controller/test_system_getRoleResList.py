from interface.Permission_Controller.data_fixture import id_min_and_max

__author__ = 'huxm855'

import os
import re

import pytest
import requests

from db_fixture.common import GlobalVar, RandomVar


class Test_system_getRoleResList(GlobalVar, RandomVar):
    ''' 根据roleId获取认证服务 '''

    @pytest.fixture()
    def before(self, login):
        self.base_url = login.host + '/system/getRoleResList'
        self.headers = login.headers
        self.params = {
            'roleId': 1,
            'authOrgId': self.GVar['match_org_userId']
        }

    def test_getRoleResList1(self, before):
        '''员工IP-根据roleId =1 获取认证服务'''

        r = requests.get(self.base_url, headers=self.headers, params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'
        assert re.search('退款管理', str(self.result))
        assert re.search('物流管理', str(self.result))
        assert re.search('服务列表', str(self.result))
        assert re.search('发布', str(self.result))
        assert re.search('购票列表', str(self.result))
        assert re.search('员工管理', str(self.result))
        assert re.search('查看赛事', str(self.result))
        assert re.search('赛事历史', str(self.result))
        assert re.search('我的订单', str(self.result))
        assert re.search('系统消息', str(self.result))
        assert re.search('赛事赞助', str(self.result))
        assert re.search('草稿箱', str(self.result))

    def test_getRoleResList2(self, before):
        '''员工IP-赛事组织，根据roleId 随机 获取认证服务'''
        minid, maxid = id_min_and_max(tablename='ip_auth_role', column='role_id')
        self.params['roleId'] = self.random_num(minid, maxid)
        r = requests.get(self.base_url, headers=self.headers, params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'

    def test_getRoleResList_train_org(self, before):
        '''员工IP-培训组织，根据roleId 随机 获取认证服务'''
        minid, maxid = id_min_and_max(tablename='ip_auth_role', column='role_id')
        self.params['roleId'] = self.random_num(minid, maxid)
        self.params['authOrgId'] = self.GVar['train_org_userId']
        r = requests.get(self.base_url, headers=self.headers, params=self.params)
        self.result = r.json()
        print(self.result)
        assert self.result['result'] == '0'


if __name__ == '__main__':
    os.system('pytest -s -v test_system_getRoleResList.py')
