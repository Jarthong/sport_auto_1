__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import random
from db_fixture.common import RandomVar, GlobalVar
from db_fixture.mysql_db import DB


class Feed_Comment_Controller(RandomVar):
    def __init__(self, column='*', table='feed', where=''):
        """连接数据库"""
        self.getdb = DB()
        self.column = column
        self.table = table
        self.where = where
        self.sql = """
                select {column} from {table}  {where}  limit 10;
                """.format(column=column, table=table, where=where)
    def results(self):
        results = self.getdb.select(self.sql)
        return results

    def result(self):
        results = self.results()
        if not results:
            result = [0] * len(self.column.split(','))
            return result
        else:
            result = random.choice(results)
            return tuple(result)


if __name__ == "__main__":
    f = Feed_Comment_Controller('f.feed_id,content_id').result()
    print(f)

    # print(';'.join(bs.menu()))
