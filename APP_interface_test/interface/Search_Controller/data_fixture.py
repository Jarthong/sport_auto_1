#!/user/bin/python
#encoding:utf-8
from db_fixture.login_token import *
from db_fixture.mysql_db import DB
from db_fixture.common import RandomVar,GlobalVar

class Search_Controller(RandomVar,GlobalVar):
    def __init__(self):
        self.getdb = DB()

    def goods_category(self):
        sql = "select * from goods_category;"
        cate_info = self.getdb.query(sql)
        cate_result = [results for results in cate_info]
        index = self.random_num(0,len(cate_result))
        catecode,catename = (cate_result[index]['cate_code'],cate_result[index]['cate_name'])
        return catecode,catename

    def feed(self):
        sql = "select * from feed limit 1,800;"
        feedinfo = self.getdb.query(sql)
        feedresult = [results for results in feedinfo]
        index = self.random_num(0,len(feedinfo))
        title = (feedresult[index]['title'])
        print(type(title))
        return title

if __name__ == '__main__':
    SC = Search_Controller()
    SC.feed()

