import os
import time
import sys



now = time.strftime("%Y-%m-%d_%H_%M_%S")
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
reportfile = parentdir + os.sep+"report"+os.sep
htmlfile = reportfile +"PC-C_testResult"
os.system('pytest -s -v --'+'html={htmlfile}.html'.format(htmlfile=htmlfile))


