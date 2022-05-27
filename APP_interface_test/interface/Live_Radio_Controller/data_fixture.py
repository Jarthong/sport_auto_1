#!/user/bin/python
#encoding:utf-8
from db_fixture.login_token import *
from db_fixture.mysql_db import DB
from db_fixture.common import RandomVar,GlobalVar

class Live_Radio(RandomVar,GlobalVar):

    def __init__(self):
        self.getdb = DB()

    def live_radio(self,USER_ID):
        """直播主表"""
        sql = "select * from live_radio t where t.USER_ID = '{USER_ID}' order by CREATE_TIME desc limit 1,20;".format(USER_ID=USER_ID)
        radio_info = self.getdb.query(sql)
        radio_result = [results for results in radio_info]
        index = self.random_num(0,len(radio_result))
        liveid = (radio_result[index]['live_id'])
        return liveid

if __name__ == '__main__':
    LR = Live_Radio()
    LR.live_radio('seedp546654')

