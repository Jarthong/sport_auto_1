#!/user/bin/python
#encoding:utf-8

from db_fixture.login_token import *
from db_fixture.mysql_db import DB
from db_fixture.common import RandomVar,GlobalVar

class Wallet_Controller(RandomVar,GlobalVar):
    """"""
    def __init__(self):
        self.getdb = DB()

    def pay_card_bin(self):
        sql = "select * from pay_card_bin limit 1,800"
        card_info = self.getdb.query(sql)
        card_result = [result for result in card_info]
        index = self.random_num(0,len(card_result))
        PLACEHOLDER = [card_result[index]['place_holder']]
        print(PLACEHOLDER)
        print("".join(PLACEHOLDER) + '75524%s' % RandomVar().random_num())
        return "".join(PLACEHOLDER)

if __name__ == '__main__':
    WC = Wallet_Controller()
    WC.pay_card_bin()