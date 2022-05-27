#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

from db_fixture.common import RandomVar,GlobalVar
from db_fixture.mysql_db import DB

class Service_Card(RandomVar,GlobalVar):
    def __init__(self):
        """连接数据库"""
        self.getdb = DB()

    def service_card(self,consumer_id=GlobalVar().GVar['q_user_id']):
        """服务卡表"""
        sql = "select card_no from service_card t  where t.consumer_id = '{consumer_id}' order by start_time desc;".format(consumer_id=consumer_id)
        results = self.getdb.select(sql)
        if not results:
            result = [0,0]
            return result
        else:
            result = []
            for x in results:
                result.append(x[0])
            return tuple(result)


if __name__ == '__main__':
    sc = Service_Card()
    sc.service_card()
    print(sc.service_card())


