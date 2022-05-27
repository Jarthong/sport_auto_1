#!/user/bin/python
#encoding:utf-8

from db_fixture.login_token import *
from db_fixture.mysql_db import DB
from db_fixture.common import RandomVar,GlobalVar

class Match_Controller(RandomVar,GlobalVar):
    def __init__(self):
        self.getdb = DB()

    def Match(self,STATUS):
        """赛事表"""
        sql = "select * from `match` where STATUS ={STATUS} limit 1,800;".format(STATUS=STATUS)
        match_info = self.getdb.query(sql)
        match_result = [ results for results in match_info ]
        index = self.random_num(0,len(match_result))
        matchid,goodcode = (match_result[index]['id'],match_result[index]['goods_code'])
        return matchid,goodcode

    def Match_Chart(self,match_name):
        sql = "select * from {match_name} where MATCH_ID IN (select MATCH_ID from match_schedule) limit 1,800;".format(match_name=match_name)
        match_chart_info = self.getdb.query(sql)
        match_chart_result = [results for results in match_chart_info]
        index = self.random_num(0,len(match_chart_result))
        matchid = (match_chart_result[index]['match_id'])
        return matchid

    def User_info(self):
        sql = "select * from user_info order by login_time DESC limit 1,50;"
        info_user = self.getdb.query(sql)
        result_user = [results for results in info_user]
        index = self.random_num(0,len(result_user))
        userid = (result_user[index]['user_id'])
        return  userid

if __name__ == "__main__":
    cx = Match_Controller()
    # print(bs.email())
    # print(bs.match_and_ip_sign_mapping())
    #bs.match_and_ip_sign_mapping()
    # print(GlobalVar.JOIN_REQUIRE)
    # cx.circle_member(18485,'seedp543681')
    cx.Match_Chart('match_chart_basketball')
