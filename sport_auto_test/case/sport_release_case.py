
import unittest
from selenium import webdriver
from time import sleep

class sport(unittest.TestCase):
    def setUp(self):
        self.d = webdriver.Chrome()
        self.d.maximize_window()
        self.d.get("http://pc.sport.com/member/login")
    def tearDown(self):
        self.d.quit()

    def test0_login_success(self):
        ''' 登陆成功，发布资讯成功 '''  # 每个用例下的第一行可以这样注释，在生成的报告的用例名称中会显示
        d = self.d
        # 登录
        d.find_element_by_name("user_id").send_keys("15915773544")
        d.find_element_by_name("user_password").send_keys("h123456")
        d.find_element_by_name("login_submit").click()
        sleep(2)
        self.assertIn('jartho',d.find_element_by_class_name("l_nickName").text)
        d.get_screenshot_as_file("./img/sport_login_success.jpg")
        # 发布资讯
        d.find_element_by_class_name("team_manage_btn").click()
        sleep(1)
        d.find_element_by_class_name("menu_subtitle").click()
        sleep(1)
        d.find_element_by_name("articleTitleInput").send_keys("添加标题测试-请在这里添加标题")
        d.switch_to.frame("ueditor_0")
        d.find_element_by_css_selector("body").send_keys("添加正文测试-请在这里输入正文请在这里输入正文请在这里输入正文")
        d.switch_to.default_content()
        d.find_element_by_id("articleDigest").send_keys("添加摘要测试-请在这里添加摘要")
        d.find_element_by_css_selector("#articleBigCategory > div.selected").click()
        d.find_element_by_css_selector("#articleBigCategory > div.opts > a:nth-child(2)").click()
        d.find_element_by_css_selector("#articleSmallCategory > div.selected").click()
        d.find_element_by_css_selector("#articleSmallCategory > div.opts > a:nth-child(2)").click()
        d.find_element_by_id("articlePublishButton").click()
        sleep(3)
        self.assertIn('保存成功',d.find_element_by_class_name("dialog_tips").text)
        d.get_screenshot_as_file("./img/sport_release_success.jpg")

    # 用户名错误
    def atest1_user_errer(self):
        '''用户名错误登陆失败'''
        self.d.find_element_by_name("username").send_keys("df")
        self.d.find_element_by_name("password").send_keys("h15915773544jx")
        self.d.find_element_by_class_name("us_Submit").click()
        self.assertIn('用户名或密码错误',self.d.find_element_by_css_selector('.boxCenterList').text)
        self.d.get_screenshot_as_file("./img/user_errer.jpg")       
        # print("测试通过：用户名错误登陆失败")
        
    # 密码错误
    def atest2_password_errer(self):
        '''密码错误登陆失败'''
        d = self.d
        d.find_element_by_name("username").send_keys("jarthong")
        d.find_element_by_name("password").send_keys("111")
        d.find_element_by_class_name("us_Submit").click()
        self.assertIn('用户名或密码错误',d.find_element_by_css_selector('.boxCenterList').text)
        d.get_screenshot_as_file("./img/password_errer.jpg")
        # print("测试通过：密码错误登陆失败")
        
    # 用户名和密码为空
    def atest3_login_null(self):
        '''用户名和密码为空登陆失败'''
        d = self.d
        d.find_element_by_name("username").send_keys("")
        d.find_element_by_name("password").send_keys("")
        d.find_element_by_class_name("us_Submit").click()
        self.assertIn('用户名不能为空',d.switch_to.alert.text)
        d.switch_to.alert.accept()
        d.get_screenshot_as_file("./img/login_null.jpg")
        # print("测试通过：用户名和密码为空登陆失败")
        

if __name__=='__main__':                        
    unittest.main()





