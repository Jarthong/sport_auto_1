__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import requests

from interface.Feed_Comment_Controller.data_fixture import Feed_Comment_Controller


def test_v1_feed_topic(login):
    ''' 获取微博所有话题信息功能接口'''
    base_url =login[0] + "/v1/feed/topic"
    r = requests.get(base_url, headers=login[-1], verify=False)
    result = r.json()
    print(result)
    json_topicName = [x['topicName'] for x in result['data']]
    topic_names = [topic_name[0] for topic_name in Feed_Comment_Controller('topic_name', table='feed_topic').results()]
    assert result['msg']==  '成功'
    assert json_topicName==  topic_names
    
if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
