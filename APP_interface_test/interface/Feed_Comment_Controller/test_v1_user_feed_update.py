__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests

from db_fixture.common import GlobalVar, RandomVar
from interface.Feed_Comment_Controller.data_fixture import Feed_Comment_Controller
#修改用户未删除的帖子
feedId1, content_id1= Feed_Comment_Controller('f.feed_id,content_id',
                                             where=" f INNER JOIN feed_content fc on f.FEED_ID=fc.FEED_ID  where f.USER_ID='{userid}' and content_type=1 and is_del=0".format(
                                                 userid=GlobalVar.GVar_hxm['user_id'])).result()
#修改用户已经删除的帖子
feedId2, content_id2= Feed_Comment_Controller('f.feed_id,content_id',
                                             where=" f INNER JOIN feed_content fc on f.FEED_ID=fc.FEED_ID  where f.USER_ID='{userid}' and content_type=1 and is_del=1".format(
                                                 userid=GlobalVar.GVar_hxm['user_id'])).result()

@pytest.mark.parametrize('feedId,content_id,num',[(feedId1,content_id1,1),(feedId2,content_id2,2)])
def test_v1_user_feed_update(login,feedId,content_id,num):
    ''' 发送微博动态功能接口'''
    base_url = login[0] + "/v1/user/feed/update"
    params = {'feedId': feedId, 'feedContents[0].content': 'autotest_content'+RandomVar().random_char_upper(),'feedContents[0].contentId': content_id, 'feedContents[0].contentType': 1, 'feedContents[0].sortNum': 1, 'feedContents[0].operationType': 2}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(params)
    print(result)
    if num==1:
        assert  result['msg']=='成功'
    else:
            assert  result['msg']== '缺少参数或参数类型不正确，请参照接口文档检查参数'




if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
