import random

from db_fixture.common import RandomVar
from db_fixture.mysql_db import DB


class GetData(RandomVar):
    def __init__(self, column='*', table='feed', where='', limt=10):
        """连接数据库"""
        self.getdb = DB()
        self.column = column
        self.table = table
        self.where = where
        self.sql = """
                select {column} from {table}  {where}  limit {limt};
                """.format(column=column, table=table, where=where, limt=limt)
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
                return 0
            else:
                result = [0] * len(self.column.split(','))
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
