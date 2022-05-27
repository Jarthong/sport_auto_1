from db_fixture.common import RandomVar, GlobalVar
from db_fixture.mysql_db import DB

__author__ = 'huxm855'
# -*- coding: utf-8 -*-


class GoodsVar:
    cateCode = ['V11', 'V12', 'V18']
    rows=[5,10,20,50]

class Goods_Cotroller(RandomVar):
    def __init__(self):
        """连接数据库"""
        self.getdb = DB()

    def goods_category(self, column='cate_code',delete_flag='N', parent_cate_code='V11'):
        """商品类目
        cate_code：(V11:体育赛事 ,V12:教育培训 ,V13众包 ,V14:文案撰写 ,V15：,V16：,V17：,V18:票务)

        """
        sql = """select {column} from goods_category where  parent_cate_code ='{parent_cate_code}'and delete_flag='{delete_flag}';

        """.format(column=column, parent_cate_code=parent_cate_code,delete_flag=delete_flag)
        results = self.getdb.select(sql)
        if not results:
            result = None
            return result
        else:
            result = []
            for x in results:
                result.append(x[0])
            return tuple(result)

    def goods(self, column='count(*)', status=0, delete_flag='N', parent_cate_code='V11'):
        """商品类目
        cate_code：(V11:体育赛事 ,V12:教育培训 ,V13众包 ,V14:文案撰写 ,V15：,V16：,V17：,V18:票务)
        按照商品类目，查出商品数据

        """
        sql = """select {column} from goods  
                    where `status`={status} 
                    and delete_flag='{delete_flag}'
                    and goods_cate_code in {goods_cate_code} ;
            """.format(column=column, status=status, delete_flag=delete_flag, goods_cate_code=self.goods_category(parent_cate_code=parent_cate_code))
        results = self.getdb.select(sql)
        if not results:
            result = 0
            return result
        else:
            result=results[0][0]
            return result
    def goods_sku(self, column='sku_code', status=0, delete_flag='N', parent_cate_code='V11',user_id=GlobalVar.GVar_hxm['user_id'],on='not in',on2='>',on3='=',num=0,buy_tiems_limit=0):
        """商品类目
        cate_code：(V11:体育赛事 ,V12:教育培训 ,V13众包 ,V14:文案撰写 ,V15：,V16：,V17：,V18:票务)
        按照goods_shopping_cart，goods_sku；查看goods库存，可购买情况
        """
        #清理垃圾数据
        clear_sql="""UPDATE goods set STATUS=1 WHERE  goods_name in (SELECT match_name FROM `match` where STATUS>=5) AND status=0"""
        self.getdb.update(clear_sql)
        sql = """
                    select {column} from goods_sku gsk inner join goods gs
                    on gsk.goods_code = gs.goods_code    
                    where gs.`status`={status} 
                    and gs.delete_flag='{delete_flag}'
                    and gs.goods_cate_code in {goods_cate_code}
                    and  gsk.sku_code  {on} (select gcat.sku_code from goods_shopping_cart gcat  where gcat.user_id='{user_id}' )
                    and gsk.stock {on2}{num}
                    and buy_tiems_limit {on3}{buy_tiems_limit}
            """.format(on=on,on2=on2,on3=on3,num=num,user_id=user_id,column=column, status=status, delete_flag=delete_flag, goods_cate_code=self.goods_category(parent_cate_code=parent_cate_code),buy_tiems_limit=buy_tiems_limit)
        results = self.getdb.select(sql)
        if not results:
            result = 0
            return result
        else:
            result=results[0]
            return result

    def goods_order(self, column='god.goods_code ,substr(god.goods_code,1,3),substr(god.goods_code,1,7),order_number,sku_code',user_id=GlobalVar.GVar_hxm['user_id'],cateCode=GoodsVar().cateCode[0],on='in',status=(1,2,3,4,5,6,7,9)):
        """订单信息
       订单状态(1待支付，2已支付，3支付失败，4已完成，5已关闭，6退款中，7已退货，9预下单)
TRANSACTION_STATUS	交易状态(0处理中，1订单录入成功，2交易成功，3交易失败，4交易处理中，5交易取消，6待交易，7待审核。8审核失败，9审核成功)
transaction_status=(0,1,2,3,4,5,6,7,8,9,'')
        """
        sql = """
            select {column}  from goods_order gor
            inner join goods_order_detail god
            on gor.id= god.order_id
             where gor.buyer_user_id='{user_id}'
             and substr(god.goods_code,1,3)='{cateCode}'
             and gor.`status` {on} {status}

            """.format(user_id=user_id,column=column,cateCode=cateCode,status=status,on=on)

        results = self.getdb.select(sql)
        if not results:
            result = [0]*5
            return result
        else:
            result=results[0]
            return result

    def goods_orders(self, column='count(*)',user_id=GlobalVar.GVar_hxm['user_id'],on='in',status=(1,2,3,4,5,6,7,9)):
        """订单信息
       订单状态(1待支付，2已支付，3支付失败，4已完成，5已关闭，6退款中，7已退货，9预下单)
TRANSACTION_STATUS	交易状态(0处理中，1订单录入成功，2交易成功，3交易失败，4交易处理中，5交易取消，6待交易，7待审核。8审核失败，9审核成功)
transaction_status=(0,1,2,3,4,5,6,7,8,9,'')
        """
        sql = """
            select {column}  from goods_order gor
             where gor.buyer_user_id='{user_id}'
             and gor.`status` {on} {status}

            """.format(user_id=user_id,column=column,status=status,on=on)
        results = self.getdb.select(sql)
        if not results:
            result = [0]*2
            return result
        else:
            result=results[0]
            return result

if __name__ == "__main__":
    bs = Goods_Cotroller()

    print(bs.goods_sku(parent_cate_code='V18'))

    # print(';'.join(bs.menu()))
