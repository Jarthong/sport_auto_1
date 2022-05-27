#!/user/bin/python
# encoding:utf-8

# __auth__=='__hq__'
from db_fixture.common import RandomVar
from db_fixture.mysql_db import DB


class Social_Controller(RandomVar):
    def __init__(self):
        self.getdb = DB()

    def social_circle(self, CREATE_USER_ID):
        sql = "select * from social_circle where CREATE_USER_ID = '{CREATE_USER_ID}' order by create_time desc limit 10".format(
            CREATE_USER_ID=CREATE_USER_ID)
        circle_info = self.getdb.query(sql)
        circle_result = [results for results in circle_info]
        index = RandomVar().random_num(0, len(circle_result))
        id = (circle_result[index]['CIRCLE_ID'])
        print(id)
        return id


if __name__ == '__main__':
    sc = Social_Controller()
    # sc.social_circle(GlobalVar().USERIDS[1])
