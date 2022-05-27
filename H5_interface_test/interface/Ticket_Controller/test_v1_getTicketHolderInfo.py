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
# class Test_GetTicketHolderInfo(object):
#     """获得取票人信息"""
#
#     @pytest.fixture()
#     def public(self,login_match):
#         self.base_url = login_match[0] + "/v1/ticket/getTicketHolderInfo"
#         self.headers = login_match[-1]
#
#     orderNumber = [Match_Controller().match(),None,'%^&']
#     @pytest.mark.parametrize('orderNumber',orderNumber)
#     def test_getobtaintype(self,public,orderNumber):
#         """
#         获得取票人信息
#         :param public:
#         :return:
#         """
#         self.params = {
#             "orderNumber": orderNumber
#         }
#         r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
#         self.result = r.json()
#         print(self.result)
#         if self.params['matchId'] is not None and self.params['matchId'] != '%^&':
#             assert self.result['msg'] == '成功'
#         elif self.params['matchId'] is None:
#             assert '参数错误' in self.result['msg']
#         elif self.params['matchId'] == '%^&':
#             assert '参数类型错误' in self.result['msg']
#
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
