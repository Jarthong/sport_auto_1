import pytest
import requests

from db_fixture.common import GlobalVar
__author__ = 'huxm855'


def test_upload_editor(login):
    '''员工IP-富文本上传控制'''
    base_url = login.host + '/upload/editor'
    headers = login.headers
    params = {
        "authOrgId": GlobalVar.GVar['match_org_userId'],
        "action": "config",
        "xUserId": headers['X-SNS-UserId'],
        "xTimestamp": headers['X-SNS-Timestamp'],
        "xSignature": headers["X-SNS-Signature"],
        "xClientType": headers["X-SNS-ClientType"],
        "noCache": headers['X-SNS-Timestamp']
    }
    r = requests.post(base_url, headers=headers, params=params)
    result = r.json()
    print(result)
    assert result['videoMaxSize'] == 102400000
    assert result['imageManagerAllowFiles'] == ['.png', '.jpg', '.jpeg', '.gif', '.bmp']

if __name__ == '__main__':
    pytest.main(['-sv',__file__])