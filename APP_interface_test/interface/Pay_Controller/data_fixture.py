from db_fixture.common import RandomVar, GlobalVar
from db_fixture.mysql_db import DB


class Pay_Controller(RandomVar, GlobalVar):
    def __init__(self):
        self.getdb = DB()

    def Good_Order(self, BUYER_USER_ID):
        """订单表"""
        sql = "select * from goods_order where BUYER_USER_ID = '{BUYER_USER_ID}' order by CREATE_DATE DESC limit 1,100;".format(
            BUYER_USER_ID=BUYER_USER_ID)
        Order_info = self.getdb.query(sql)
        Order_result = [results for results in Order_info]
        index = self.random_num(0, len(Order_result))
        ordernumber = (Order_result[index]['order_number'])
        return ordernumber
