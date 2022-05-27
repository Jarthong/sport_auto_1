#!/user/bin/python
#encoding:utf-8

#__auth__=='__hq__'
from db_fixture.common import RandomVar
from db_fixture.mysql_db import DB


class Match_Controller(RandomVar):
    def __init__(self):
        self.getdb = DB()

    def match(self):
        sql = "select * from `match` limit 10;"
        match_info = self.getdb.query(sql)
        match_result = [results for results in match_info]
        index = self.random_num(0,len(match_result))
        ID = (match_result[index]['ID'])
        return ID

if __name__ == '__main__':
    mc = Match_Controller()
    mc.match()

