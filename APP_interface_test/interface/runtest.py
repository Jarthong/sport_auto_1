#!/user/bin/python
#encoding:utf-8

#__auth__=='__hq__'

import os,time


# 获取路径
now = time.strftime("%Y-%m-%d_%H_%M_%S")
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
casedir = parentdir + "interface"
reportfile = parentdir + "\\report\\"
htmlfile = reportfile +"APP_testResult"

def add_case(case_path=casedir, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = os.system('pytest -s -v --'+'html={htmlfile}.html'.format(htmlfile=htmlfile))
    return discover

if __name__ == "__main__":
    # 用例集合
    cases = add_case()