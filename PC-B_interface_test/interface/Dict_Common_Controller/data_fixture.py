from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'
def ReadMsgTotal(to_org_user_id=GlobalVar().GVar['match_org_userId'], to_user_id=GlobalVar().GVar['user_id'],
                 user_status=1, platform=2):
    # """系统消息
    # USER_STATUS	消息状态，1：未阅读，2：未回复，3：已拒绝，4：已同意，5：已阅读，6：已回复
    # PLATFORM	1,C端 2,B端
    # """
    sql = """select count(*) from msg_user_mapping where  to_org_user_id='{to_org_user_id}' and to_user_id='{to_user_id}' and user_status={user_status} and platform ={platform};

        """.format(to_org_user_id=to_org_user_id, to_user_id=to_user_id, user_status=user_status, platform=platform)
    print(sql)
    result =GetData(sql=sql).result()
    return result

def menu(column='ser.service_code', ip_cate_id=510, device_type=1):
    # """根据 组织类型,设备类型加载 菜单
    # 客户端类型：1.PC，2.android，3.iOS，4.H5，5.APP(包含2、3)，6.移动端（包含2、3、4）
    # -- 0 是系统默认
    # -- 200	体育协会
    # -- 202	俱乐部
    # -- 201	体育培训
    # -- 510	体育赛事
    # """
    sql = """
        select {column} from  ip_auth_service ser
        inner join ip_auth_service_cate sca
        on ser.service_code = sca.service_code
        inner join ip_auth_service_info ip
        on ser.service_code = ip.service_code
        where ser.status=1 and ser.service_type=1  and  ser.parent_code=0
        and ip.device_type={device_type}
        and sca.ip_cate_id  in (0,{ip_cate_id});
""".format(ip_cate_id=ip_cate_id, device_type=device_type, column=column)
    result =GetData(sql=sql).results()
    return result

