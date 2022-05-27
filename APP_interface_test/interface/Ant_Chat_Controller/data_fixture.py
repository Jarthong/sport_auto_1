__author__ = 'chenhh1334'
# -*- coding: utf-8 -*-

import random

from db_fixture.common import RandomVar, GlobalVar
from db_fixture.mysql_db import DB


class Ant_Chat_Controller(RandomVar, GlobalVar):
    def __init__(self):
        self.getdb = DB()

    def org_info(self, column='org_user_id', user_id=GlobalVar.GVar_chh['userid']):
        """
        用 group_member表 和 group_info表 查询出有效且已加入组织的组织id :ORG_USER_ID
        """
        sql = "select {column} from group_member t1, group_info t2 WHERE t1.group_id = t2.group_id AND t1.user_id = '{user_id}'".format(
            column=column, user_id=user_id)
        results = self.getdb.select(sql)
        if results:
            result = random.choice(results)
            return result
        else:
            result = 0
            return result

    def chat_room_member(self, column='room_id', user_id=GlobalVar.GVar_chh['userid']):
        """
       通过chat_room_member 聊天室成员表，查询出room_id
        """
        sql = "SELECT {column} from chat_room_member WHERE user_id = '{user_id}' ".format(column=column,
                                                                                          user_id=user_id)
        results = self.getdb.select(sql)
        if results:
            result = random.choice(results)
            print(result)
            return result
        else:
            result = 0
            return result

    def chat(self, column='', table='', where=''):
        """
       聊天室成员表
        """
        sql = "SELECT {column} from {table} {where} ".format(column=column, table=table, where=where)
        results = self.getdb.select(sql)
        if results:
            result = random.choice(results)
            return result
        else:
            result = 0
            return result


if __name__ == "__main__":
    go = Ant_Chat_Controller()
    print(go.chat(column='ROOM_ID, USER_ID', table='chat_room_member'))
