#!/user/bin/python
#encoding:utf-8
from db_fixture.login_token import *
from db_fixture.mysql_db import DB
from db_fixture.common import RandomVar,GlobalVar

class Guest_Controller(RandomVar,GlobalVar):

    def __init__(self):
        self.getdb = DB()

    def espn(self):
        """频道表"""
        sql = "select * from espn limit 1,800;"
        espn_info = self.getdb.query(sql)
        espn_result = [results for results in espn_info]
        index = self.random_num(0,len(espn_result))
        espncode = (espn_result[index]['espn_code'])
        return espncode

if __name__ == '__main__':
    GC = Guest_Controller()
    GC.espn()

