import random

from db_fixture.common import RandomVar
from db_fixture.mysql_db import DB


class GetData(RandomVar):
    def __init__(self, column='*', table='feed', where='1', limt=10,sql=None):
        """连接数据库"""
        self.getdb = DB()
        self.column = column
        self.table = table
        self.where = where
        if sql is None:
            self.sql = """
                    select {column} from {table} where {where}  limit {limt};
                    """.format(column=column, table=table, where=where, limt=limt)
        else:
            self.sql=sql
        self.__results = self.getdb.select(self.sql)

    def result(self):
        """获取查询结果中的一条记录处理
        1.查询结果无值
        2.查询结果有值
        """
        results = self.__results
        if not results:  # 查询结果：0条记录
            if len(self.column.split(
                    ',')) == 1:
                return None
            else:
                result = [None] * len(self.column.split(','))
                return result
        else:
            result = random.choice(results)  # 在查询结果中随机获取一条记录
            if len(
                    result) > 1:
                return result
            else:
                return result[0]  # 在tuple取出值

    def results(self):
        # 查出所有记录
        results = self.__results
        if len(self.column.split(',')) == 1:
            return tuple(x[0] for x in results)
        else:
            results_values =[]
            for lens in range(len(self.column.split(','))):
                column_values =tuple(column[lens] for column in results)
                results_values.append(column_values)
            return results_values

    def result_original(self):
        return  self.__results
    def results_query(self):

        # 查出所有记录
        try:
            results = self.getdb.query(self.sql)
            result = random.choice(results)
            return result
        except IndexError:
            return None
    def results_querys(self):
        # 查出所有记录
        results = self.getdb.query(self.sql)
        return results
if __name__ == '__main__':
    sql="""SELECT FEED_ID,USER_ID,DERVICE_TYPE FROM feed where USER_ID='seedp50'"""
    print(DB().query(sql))
