# -*- coding: utf-8 -*-
__author__ = 'huxm855'

import random

from db_fixture.common import RandomVar, GlobalVar
from db_fixture.mysql_db import DB

class GoodsVar:
    cateCode = ['V11', 'V12', 'V18']
    rows = [10,20,50,100]

class Device_Info_Controller(RandomVar):
    def __init__(self):
        """连接数据库"""
        self.getdb = DB()
    def user_info(self,column='*',user_id=GlobalVar.GVar_hxm['user_id'],on='='):
        """获取用户信息"""
        sql = """
                select {column} from user_info where user_id {on}'{user_id}' limit 10;

                """.format(column=column, user_id=user_id,on=on)
        results = self.getdb.select(sql)
        if not results:
            result = [0, 0]
            return result
        else:
            result = []
            for x in results:
                result.append(x)
            return tuple(result)

    def user_token(self, column='ant_token',user_id=GlobalVar.GVar_hxm['user_id']):
        """获取用户token
        """
        sql = """select {column} from user_token where user_id='{user_id}'and device_type=5  ;

        """.format(column=column, user_id=user_id)
        results = self.getdb.select(sql)
        return  results[0][0]

    def user_delivery_address(self, column='count(*)',user_id=GlobalVar.GVar_hxm['user_id']):
        """用户收货地址
        """
        sql = """
        select {column} from user_delivery_address where user_id='{user_id}' order by create_time desc;

        """.format(column=column, user_id=user_id)
        results = self.getdb.select(sql)
        if not results:
            result = [0,0]
            return result
        else:
            result = []
            for x in results:
                result.append(x[0])
            return tuple(result)
    def user_favorite(self, column='*',user_id=GlobalVar.GVar_hxm['user_id'],other=''):
        """收藏地址
        """
        sql = """
        select {column} from user_favorite where user_id='{user_id}'  {other}  order by create_time desc;

        """.format(column=column, user_id=user_id,other=other)
        results = self.getdb.select(sql)
        if not results:
            result = [0,0]
            return result
        else:
            result = []
            for x in results:
                result.append(x)
            return tuple(result)[0]

    def delete_user_delivery_address(self,user_id=GlobalVar.GVar_hxm['user_id']):
        """
        用户收货地址删除
        """
        sql = """
        delete from user_delivery_address where user_id='{user_id}' 

        """.format(user_id=user_id)
        self.getdb.delete(sql)



    def user_follow(self, column, user_id=GlobalVar.GVar_hxm['user_id'], other=''):
        """收藏地址
        """
        sql = """
        select {column} from user_follow where user_id='{user_id}'  {other}  ;
    
        """.format(column=column, user_id=user_id, other=other)
        results = self.getdb.select(sql)
        if not results:
            result = [0, 0]
            return result
        else:

            return random.choice(results)

    def snsunion_role_res(self):
        """角色权限关联表
        """
        sql = """
        select distinct(role_id) from snsunion_role_res ;
        """
        results = self.getdb.select(sql)
        return random.choice(results)

if __name__ == "__main__":
    bs = Device_Info_Controller()
    print(Device_Info_Controller().user_follow(column='followed_user_id'))


    # print(';'.join(bs.menu()))
