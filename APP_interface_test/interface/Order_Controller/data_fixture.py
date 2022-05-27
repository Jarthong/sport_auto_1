#!/user/bin/python
#encoding:utf-8

from db_fixture.login_token import *
from db_fixture.mysql_db import DB
from db_fixture.common import RandomVar,GlobalVar

class Order_Controller(RandomVar,GlobalVar):
    def __init__(self):
        self.getdb = DB()

    def Good_Order(self,BUYER_USER_ID,STATUS):
        """订单表"""
        sql = "select * from goods_order where BUYER_USER_ID = '{BUYER_USER_ID}' and STATUS = {STATUS} order by CREATE_DATE DESC limit 1,100;".format(BUYER_USER_ID=BUYER_USER_ID,STATUS=STATUS)
        Order_info = self.getdb.query(sql)
        Order_result = [results for results in Order_info]
        index = self.random_num(0,len(Order_result))
        ordernumber = (Order_result[index]['order_number'])
        return ordernumber

    def Goods_Sku(self,STATUS,MIN_TEAM_MEMBER):  # （0，草稿，1，待审核，2，审核不通过，3，审核通过、4、报名中，5、报名截止，6、进行中，7、已结束,8.提前关闭）
        sql = "SELECT b.SKU_CODE,c.* FROM goods a,goods_sku b,`match` c WHERE	a.GOODS_CODE = b.GOODS_CODE and b.GOODS_CODE = c.GOODS_CODE and a.`STATUS` = '0' AND a.CHECK_STATUS = '1' and c.MIN_TEAM_MEMBER = '{MIN_TEAM_MEMBER}' and c.`STATUS` = '{STATUS}' limit 1,800;".format(STATUS=STATUS,MIN_TEAM_MEMBER=MIN_TEAM_MEMBER)
        Sku_info = self.getdb.query(sql)
        Sku_result = [results for results in Sku_info]
        index = self.random_num(0,len(Sku_info))
        Sku_code,STATUS = (Sku_result[index]['sku_code'],Sku_result[index]['status'])
        return Sku_code

    def Goods_Sku_null(self,STATUS):  # （0，草稿，1，待审核，2，审核不通过，3，审核通过、4、报名中，5、报名截止，6、进行中，7、已结束,8.提前关闭）
        sql = "SELECT b.SKU_CODE,c.* FROM goods a,goods_sku b,`match` c WHERE	a.GOODS_CODE = b.GOODS_CODE and b.GOODS_CODE = c.GOODS_CODE and a.`STATUS` = '0' AND a.CHECK_STATUS = '1' and c.MIN_TEAM_MEMBER is null and c.`STATUS` = '{STATUS}' limit 1,800;".format(STATUS=STATUS)
        Sku_info = self.getdb.query(sql)
        Sku_result = [results for results in Sku_info]
        index = self.random_num(0,len(Sku_info))
        Sku_code,STATUS = (Sku_result[index]['sku_code'],Sku_result[index]['status'])
        return Sku_code

    def Goods_Sku_status(self,STATUS):  # （0，草稿，1，待审核，2，审核不通过，3，审核通过、4、报名中，5、报名截止，6、进行中，7、已结束,8.提前关闭）
        sql = "select a.SKU_CODE,b.* from goods_sku a,goods b where a.GOODS_CODE = b.GOODS_CODE and b.STATUS = {STATUS};".format(STATUS=STATUS)
        Sku_info = self.getdb.query(sql)
        Sku_result = [results for results in Sku_info]
        index = self.random_num(0,len(Sku_info))
        Sku_code,STATUS = (Sku_result[index]['sku_code'],Sku_result[index]['status'])
        return Sku_code







if __name__ == "__main__":
    go = Order_Controller()
    # # go.Good_Order(GlobalVar().ORG_USERIDS[0],2)
    # go.Goods_Sku_null(1)
    # skuCode = [Order_Controller().Goods_Sku(4,1),Order_Controller().Goods_Sku_null(1)]
    # print(skuCode)
    go.Good_Order('seedp10',2)



