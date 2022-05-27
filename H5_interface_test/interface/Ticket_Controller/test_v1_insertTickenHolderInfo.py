# #!/user/bin/python
# #encoding:utf-8
# #__auth__=='__hq__'
#
# import pytest,os
# from test_interface.Match_Controller.Sql_Conf import *
# from  db_fixture.login_token import *
# import  urllib3
# from urllib3.exceptions import InsecureRequestWarning
# urllib3.disable_warnings(InsecureRequestWarning)
#
#
# class Test_InsertTicketHolderInfo(object):
#     """新增取票人信息"""
#     orderNumber = [26603211328061449]
#     @pytest.mark.parametrize('orderNumber',orderNumber)
#     def test_insertticketholderinfo(self,login_match):
#         """
#         新增取票人信息
#         :param public:
#         :return:
#         """
#         self.base_url = login_match[0] + "/v1/ticket/insertTicketHolderInfo"
#         self.second_url = login_match[0] + "/v1/order/orderInfo"
#         self.headers = login_match[-1]
#         a = requests.post(self.second_url,headers = self.headers,verify=False,params={
#             "addressId":599,
#             "detailList[0].skuCode":'V181001_20180305165932_2954_20180305165932_4162',
#             "detailList[0].quantity":'1'
#         })
#         self.result2 = a.json()
#         t = self.result2['data']['orderNumber']
#         self.params = {
#             "name":'蓉儿',
#             "mobile":17688536737,
#             "idNo":440305198801011137,
#             "address":'北京市北京市辖区东城区旅途点滴',
#             "orderNumber":t,
#             "obtainType":'比赛当天现场取票'
#         }
#         r = requests.post(self.base_url,headers = self.headers,verify=False,params=self.params)
#         self.result = r.json()
#         print(self.result)
#
# if __name__ == '__main__':
#     os.system('pytest -v -s {file}'.format(file=__file__))
#
#
#
#
#
#
#
#
#
