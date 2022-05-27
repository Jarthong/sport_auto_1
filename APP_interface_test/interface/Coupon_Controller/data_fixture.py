#!/user/bin/python
#encoding:utf-8

from db_fixture.login_token import *
from db_fixture.mysql_db import DB
from db_fixture.common import RandomVar,GlobalVar

class Coupon_Controller(RandomVar,GlobalVar):
    """"""
    def __init__(self):
        self.getdb = DB()

    def coupon(self,USER_ID=GlobalVar().ORG_USERIDS[0]):
        """优惠券数据表"""
        sql = "select * from coupon t where t.USER_ID='{USER_ID}' order by t.create_time desc limit 1,800;".format(USER_ID=USER_ID)
        coupon_info = self.getdb.query(sql)
        coupon_result = [results for results in coupon_info]
        index = self.random_num(0,len(coupon_result))
        code_id,batch_id = (coupon_result[index]['code_id'],coupon_result[index]['batch_id'])
        return code_id,batch_id

    def coupon_code(self,CODE_STATUS,USER_ID=GlobalVar().ORG_USERIDS[0]):
        """
        优惠券兑换码数据表
        CODE_STATUS:1,未使用,2已使用,3使用中(未用完),4已过期,5已作废
        """
        sql = "SELECT a.* from coupon_code a LEFT JOIN coupon b ON a.BATCH_ID = b.BATCH_ID where b.USER_ID = '{USER_ID}' and a.CODE_STATUS = {CODE_STATUS};".format(USER_ID=USER_ID,CODE_STATUS=CODE_STATUS)
        coupon_code_info = self.getdb.query(sql)
        coupon_code_result = [results for results in coupon_code_info]
        index = self.random_num(0,len(coupon_code_result))
        BATCH_ID,EXCHANGE_CODE = (coupon_code_result[index]['batch_id'],coupon_code_result[index]['exchange_code'])
        return BATCH_ID,EXCHANGE_CODE

    def coupon_code_not(self,COUPON_STATUS,CODE_STATUS,USER_ID=GlobalVar().ORG_USERIDS[0]):
        """未领过的优惠券"""
        sql = "select * from coupon_code t where t.BATCH_ID in (select ID from coupon_batch a where a.COUPON_STATUS = {COUPON_STATUS}) and " \
              "t.BATCH_ID not in (select BATCH_ID from coupon where USER_ID='{USER_ID}') and t.CODE_STATUS = {CODE_STATUS};".format(COUPON_STATUS=COUPON_STATUS,USER_ID=USER_ID,CODE_STATUS=CODE_STATUS)
        coupon_not_codeinfo = self.getdb.query(sql)
        coupon_not_coderesult = [results for results in coupon_not_codeinfo]
        index = self.random_num(0,len(coupon_not_coderesult))
        EXCHANGE_CODE = (coupon_not_coderesult[index]['exchange_code'])
        return EXCHANGE_CODE


if __name__ == '__main__':
    cp = Coupon_Controller()
    cp.coupon_code(2)
    print(cp.coupon_code(2)[0])



