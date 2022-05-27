# -*- coding: utf-8 -*-
from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

'''
#定义发送邮件
def send_mail(file_new):
    f = open(file_new, 'rb').read()
    att = MIMEText(f, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename=test_result.html'
    msgRoot = MIMEMultipart("related")
    msgRoot['Subject'] = '自动化测试报告'
    msgRoot.attach(att)
    smtpHost = 'smtp.qq.com'  
    smtpPort = '25'  
    sslPort  = '465'  
    fromMail = '发件人qq邮箱'  
    toMail   = '收件人qq邮箱'  
    username = '发件人qq邮箱'  
    password = '密码（！QQ邮箱通过第三方发送邮件需要获取授权码）'  
    smtp = smtplib.SMTP(smtpHost,smtpPort)  
    smtp.ehlo()  
    smtp.starttls()  
    smtp.ehlo()  
    smtp.login(username,password)
    smtp.sendmail(fromMail,toMail,msgRoot.as_string())  
    smtp.close()  
'''

# 查找目录
def new_report(testreport):
	lists = os.listdir(testreport)
	lists.sort(key=lambda fn : os.path.getmtime(testreport + "\\" + fn))
	file_new = os.path.join(testreport,lists[-1])
	return file_new



if __name__ == '__main__':
	test_dir = './case'
	test_report = './report'
	discover = unittest.defaultTestLoader.discover(test_dir,pattern = '*_case.py')
	now = time.strftime("%Y-%m-%d_%H_%M_%S")
	filename = test_report + '\\' + now + 'result.html'

	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream = fp ,title = "自动化测试报告",description = '环境:WIN7  浏览器:Chrome')
	runner.run(discover)
	fp.close()

	new_report = new_report(test_report)
	# send_mail(new_report)





