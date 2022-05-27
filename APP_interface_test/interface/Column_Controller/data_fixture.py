# -*- coding: utf-8 -*-
__author__ = 'huxm855'


from db_fixture.common import RandomVar, GlobalVar
from db_fixture.mysql_db import DB

class Column_Controller(RandomVar,GlobalVar):
    def __init__(self):
        """连接数据库"""
        self.getdb = DB()

    def homepage_column(self, column='column_title',device_type=2,status=1,column_type=1):
        """首页栏目管理
        COLUMN_TYPE	栏目类型:首页栏目1;专题类栏目2
        STATUS	是否显示栏目本身： 0 ，不显示 ；  1， 显示        """
        sql = """select {column} from homepage_column where device_type in ({device_type})and status ={status} and column_type={column_type};

        """.format(column=column, device_type=device_type,status=status,column_type=column_type)
        results = self.getdb.select(sql)
        if not results:
            result = 0
            return result
        else:
            return results



if __name__ == "__main__":
    bs = Column_Controller()
    # print(bs.goods_category(parent_cate_code='V12'))
    # print(bs.goods(parent_cate_code='V18'))
    a =bs.homepage_column()
    print(a)

    # print(';'.join(bs.menu()))
