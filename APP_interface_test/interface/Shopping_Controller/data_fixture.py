__author__ = 'huxm855'
# -*- coding: utf-8 -*-
from db_fixture.common import RandomVar, GlobalVar
from db_fixture.mysql_db import DB

class Shopping_Controller(RandomVar,GlobalVar):
    def __init__(self):
        """连接数据库"""
        self.getdb = DB()

    def goods_shopping_cart(self, column='sku_code',status=1, user_id=GlobalVar().GVar_hxm['user_id']):
        """商品类目
        cate_code：(V11:体育赛事 ,V12:教育培训 ,V13众包 ,V14:文案撰写 ,V15：,V16：,V17：,V18:票务)

        """
        sql = """select {column} from goods_shopping_cart where  status= {status} and user_id='{user_id}';

        """.format(column=column, status=status,user_id=user_id)
        results = self.getdb.select(sql)
        if not results:
            result = [0,0]
            return result
        else:
            result = []
            for x in results:
                result.append(x[0])
            return tuple(result)
    def init_goods_shopping_cart(self,status=1, user_id=GlobalVar().GVar_hxm['user_id']):
        """ 还原删除删除的购物车数据 """
        sql = """update  goods_shopping_cart set status= {status} where user_id='{user_id}';

        """.format(status=status,user_id=user_id)
        self.getdb.update(sql)


if __name__ == "__main__":
    bs = Shopping_Controller()
    # print(bs.goods_category(parent_cate_code='V12'))
    # print(bs.goods(parent_cate_code='V18'))
    print(Shopping_Controller().goods_shopping_cart(column='id')[0])

    # print(';'.join(bs.menu()))
