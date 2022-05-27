#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import os,json,ast
import pytest
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Article_Comment_Contro.data_fixture import Article_Information

urllib3.disable_warnings(InsecureRequestWarning)


articleId = [Article_Information().article(1)[0]]
@pytest.mark.parametrize('articleId',articleId)
def test_api_article_getArticleInfo(login_train,articleId):
    ''' 根据 商品code 获取商品列表'''
    base_url = login_train[0] + "/v1/article/getArticleInfo"
    params = {
        'lang': 'zh_CN',
        'articleId': articleId
    }
    r = requests.get(base_url, headers=login_train[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if params['articleId'] is not None:
        assert result['msg'] == '成功'
        assert result['result'] == '0'

if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))







