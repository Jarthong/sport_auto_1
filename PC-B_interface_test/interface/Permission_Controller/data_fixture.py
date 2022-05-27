from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'


def get_EmployeeId(column='*', is_creator=0, user_id=GlobalVar().GVar['match_org_userId'],
                   login_user_id=GlobalVar().GVar['user_id']):
    # """����ҳ�һ��Ա����Ϣ"""
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
    # """����ҳ�һ����֯�µ�role_id,ip_cate_id=510 Ϊ���£�201Ϊ��ѵ"""
    sql = """select role_id from ip_auth_role where (user_id in ('{group_user_id}','{login_user_id}') or user_id is null) and ip_cate_id ='{ip_cate_id}' and role_type in (0,1);""".format(
        group_user_id=group_user_id, login_user_id=login_user_id, ip_cate_id=ip_cate_id)
    return GetData(sql=sql).result()


def get_UnemployeeId(column='user_id', group_user_id=GlobalVar().GVar['match_org_userId'],
                     login_user_id=GlobalVar().GVar['user_id'], auth_type=1):
    # """����ҳ�һ����Ա����Ϣ,auth_type 1���ˣ� 2��֯"""
    sql = """select {column} from user_info 
        where
        user_id not in (select user_id from group_member gm where group_id in (select group_id from  group_member where is_creator=1 and user_id='{group_user_id}') and user_id !='{login_user_id}') 
        and auth_type={auth_type} 
        and {column} is not null
		limit 10,100;
        """.format(column=column, group_user_id=group_user_id, login_user_id=login_user_id, auth_type=auth_type)
    return GetData(sql=sql).result()


def id_min_and_max(column='id', tablename='`match`'):
    # """��ѯ�� max��min ID
    # ����״̬��0���ݸ壬1������ˣ�2����˲�ͨ����3�����ͨ����4�������У�5��������ֹ��6�������У�7���ѽ���,8.��ǰ�رգ�
    # results[0] Ϊ�ֶ�match_id   results[21] Ϊ�ֶ�status
    # """
    sql = "select min({column}),max({column}) from {tablename};".format(tablename=tablename, column=column)

    return GetData(sql=sql).result()


def menu(column='ser.service_code', ip_cate_id=510, device_type=1):
    # """���� ��֯����,�豸���ͼ��� �˵�
    # �ͻ������ͣ�1.PC��2.android��3.iOS��4.H5��5.APP(����2��3)��6.�ƶ��ˣ�����2��3��4��
    # -- 0 ��ϵͳĬ��
    # -- 200	����Э��
    # -- 202	���ֲ�
    # -- 201	������ѵ
    # -- 510	��������
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
