# -*- coding:utf-8 -*-
import configparser
import os,sys

# 如果没有安装mysql 模块，则启动pip安装
try:
    import mysql.connector
except:
    os.system('pip install wheel')
    os.system(
        'pip install http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.zip#md5=3df394d89300db95163f17c843ef49df')

base_dir = str(os.path.dirname(os.path.dirname(__file__))).replace('\\', '/')

#测试库
file_path = base_dir + "/main/db_config.ini"
db = 'interface_test'

#开发库
# file_path = base_dir + "/main/db_config2.ini"
# db = 'sportsdb'

config = configparser.ConfigParser()

# 从配置文件 main\db_config.ini 中读取数据库服务器IP、域名，端口
config.read(file_path, encoding="utf-8")


class DB:
    '''配置数据库IP，端口等信息，获取数据库连接'''

    def __init__(self):
        # 连接mysql，获取游标
        try:
            self.conn = mysql.connector.connect(**(dict(config[db])))
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('%s', e)
            sys.exit()

    # 连接mysql，执行select

    def select(self, sql):

        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(' select  failed.',sql)
            print(e)

    # 连接mysql，执行insert

    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()

        except Exception as e:
            print("insert failed.",sql)
            print(e)
            self.conn.rollback()

    # 连接mysql，执行update

    def update(self, sql):

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as  e:
            print("update failed",sql)
            print(e)
            self.conn.rollback()

    # 执行删除sql
    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()

        except Exception as e:
            print("delete failed.")
            print(e)
            self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def query(self, sql):
        self.cursor.execute(sql)
        index = self.cursor.description
        result = []
        for res in self.cursor.fetchall():
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = res[i]
            result.append(row)
        return result




if __name__ == "__main__":
    # 执行sql
    getdb = DB()
    getdb.close()