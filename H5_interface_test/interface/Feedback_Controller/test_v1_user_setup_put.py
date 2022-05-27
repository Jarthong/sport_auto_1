
__author__ = 'huxm855'

import os
import pytest
import requests
#状态1,所有人；2,我关注的人；3关闭
status=range(1,4)
#是，否
status2=range(2)

@pytest.mark.parametrize('allowComment',status)
@pytest.mark.parametrize('commentImage',status2)

def test_v1_user_setup(login,allowComment,commentImage):
    ''' 修改用户隐私信息设置'''
    base_url =login.host + "/v1/user/setup"
    params={'allowComment': allowComment, 'commentImage': commentImage}
    r = requests.put(base_url, headers=login.headers, params=params, verify=False)
    result = r.json()
    print(result)
    assert result['msg']==  '成功'
    


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))