#!/user/bin/python
#encoding:utf-8

from db_fixture.login_token import *
from db_fixture.mysql_db import DB
from db_fixture.common import RandomVar,GlobalVar

class Community_Controller(RandomVar,GlobalVar):
    def __init__(self):
        """连接数据库"""
        self.getdb = DB()

    def social_circle(self):
        """圈子信息表"""
        sql = "select * from social_circle order by create_time desc limit 1,800;"
        circle_info = self.getdb.query(sql)
        circle_results = [result for result in circle_info]
        index = self.random_num(0,len(circle_results))
        circleid,circlename = (circle_results[index]['circle_id'],circle_results[index]['circle_name'])
        # print(circleid,circlename)
        return circleid,circlename

    def circle_member(self,CIRCLE_ID,USER_ID):
        """圈子成员表"""
        sql = "select * from circle_members where CIRCLE_ID = '{CIRCLE_ID}' and USER_ID != '{USER_ID}'order by CREATE_TIME desc;".format(CIRCLE_ID=CIRCLE_ID,USER_ID=USER_ID)
        member_info = self.getdb.query(sql)
        member_result = [results for results in member_info]
        index = self.random_num(0,len(member_result))
        member_id,circle_id,user_id = (member_result[index]['member_id'],member_result[index]['circle_id'],member_result[index]['user_id'])
        return member_id,circle_id,user_id

    def feed_circle(self,CIRCLE_ID):
        """帖子圈子表"""
        sql = "select * from feed_circle where CIRCLE_ID = '{CIRCLE_ID}' limit 1,800;".format(CIRCLE_ID=CIRCLE_ID)
        feed_info = self.getdb.query(sql)
        feed_result = [results for results in feed_info]
        index = self.random_num(0,len(feed_result))
        FEEDID,CIRCLEID = (feed_result[index]['feed_id'],feed_result[index]['circle_id'])
        return FEEDID,CIRCLEID



if __name__ == "__main__":
    cx = Community_Controller()
    # print(bs.email())
    # print(bs.match_and_ip_sign_mapping())
    #bs.match_and_ip_sign_mapping()
    # print(GlobalVar.JOIN_REQUIRE)
    # cx.circle_member(18485,'seedp543681')
    cx.feed_circle(18485)

