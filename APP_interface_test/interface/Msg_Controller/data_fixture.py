#!/user/bin/python
#encoding:utf-8

from db_fixture.login_token import *
from db_fixture.mysql_db import DB
from db_fixture.common import RandomVar,GlobalVar

class Msg_Controller(RandomVar,GlobalVar):
    def __init__(self):
        self.getdb = DB()

    def org_info(self,ORG_TYPE):
        """
        组织基础信息表
        :return:
        """
        sql = "select * from org_info t where t.ORG_TYPE in (select IP_CATE_ID from ip_auth_cate) and t.ORG_TYPE = {ORG_TYPE};".format(ORG_TYPE=ORG_TYPE)
        orginfo = self.getdb.query(sql)
        orgresult = [ results for results in orginfo ]
        index = self.random_num(0,len(orgresult))
        org_id = (orgresult[index]['ORG_ID'])
        return org_id

    def msg_info(self):
        """
        组织基础信息表
        :return:
        """
        sql = "select * from msg_info limit 1,800;"
        msginfo = self.getdb.query(sql)
        msgresult = [ results for results in msginfo ]
        index = self.random_num(0,len(msgresult))
        msgtype = (msgresult[index]['msg_type'])
        return msgtype

    def msg_user_mapping(self,FROM_USER_ID):
        sql = "select * from msg_user_mapping t where t.FROM_USER_ID = '{FROM_USER_ID}' order by t.CREATE_TIME desc;".format(FROM_USER_ID=FROM_USER_ID)
        msginfo = self.getdb.query(sql)
        msgresult = [results for results in msginfo]
        index = self.random_num(0,len(msgresult))
        ID = (msgresult[index]['id'])
        return ID

    def msg_info1005(self,msg_type):
        sql = "select * from msg_info where msg_type = '{msg_type}' order by  CREATE_TIME desc limit 5;".format(msg_type=msg_type)
        info1005 = self.getdb.query(sql)
        result1005 = [results for results in info1005]
        index = self.random_num(0,len(result1005))
        msg_id = (result1005[index]['msg_id'])
        return msg_id


if __name__ == '__main__':
    MC = Msg_Controller()
    MC.msg_info1005(1005)

