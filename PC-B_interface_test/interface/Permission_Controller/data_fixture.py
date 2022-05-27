from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'


def get_EmployeeId(column='*', is_creator=0, user_id=GlobalVar().GVar['match_org_userId'],
                   login_user_id=GlobalVar().GVar['user_id']):
    # """随机找出一个员工信息"""
    sql = """select {column} 
        from group_member gm 
        where 
        group_id in (select group_id from  group_member where is_creator=1 and user_id='{user_id}')
        and is_creator={is_creator}
        and user_id !='{login_user_id}'
        """.format(column=column, is_creator=is_creator, user_id=user_id, login_user_id=login_user_id)
    return GetData(sql=sql).result()


def get_emplo_roleId(group_user_id=GlobalVar().GVar['match_org_userId'],
                     login_user_id=GlobalVar().GVar['user_id'], ip_cate_id='510'):
    # """随机找出一个组织下的role_id,ip_cate_id=510 为赛事，201为培训"""
    sql = """select role_id from ip_auth_role where (user_id in ('{group_user_id}','{login_user_id}') or user_id is null) and ip_cate_id ='{ip_cate_id}' and role_type in (0,1);""".format(
        group_user_id=group_user_id, login_user_id=login_user_id, ip_cate_id=ip_cate_id)
    return GetData(sql=sql).result()


def get_UnemployeeId(column='user_id', group_user_id=GlobalVar().GVar['match_org_userId'],
                     login_user_id=GlobalVar().GVar['user_id'], auth_type=1):
    # """随机找出一个非员工信息,auth_type 1个人， 2组织"""
    sql = """select {column} from user_info 
        where
        user_id not in (select user_id from group_member gm where group_id in (select group_id from  group_member where is_creator=1 and user_id='{group_user_id}') and user_id !='{login_user_id}') 
        and auth_type={auth_type} 
        and {column} is not null
		limit 10,100;
        """.format(column=column, group_user_id=group_user_id, login_user_id=login_user_id, auth_type=auth_type)
    return GetData(sql=sql).result()


def id_min_and_max(column='id', tablename='`match`'):
    # """查询表 max，min ID
    # 赛事状态（0，草稿，1，待审核，2，审核不通过，3，审核通过、4、报名中，5、报名截止，6、进行中，7、已结束,8.提前关闭）
    # results[0] 为字段match_id   results[21] 为字段status
    # """
    sql = "select min({column}),max({column}) from {tablename};".format(tablename=tablename, column=column)

    return GetData(sql=sql).result()


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
    return GetData(sql=sql).results()
