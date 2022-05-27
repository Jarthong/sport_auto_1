from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'
def ReadMsgTotal(to_org_user_id=GlobalVar().GVar['match_org_userId'], to_user_id=GlobalVar().GVar['user_id'],
                 user_status=1, platform=2):
    # """ϵͳ��Ϣ
    # USER_STATUS	��Ϣ״̬��1��δ�Ķ���2��δ�ظ���3���Ѿܾ���4����ͬ�⣬5�����Ķ���6���ѻظ�
    # PLATFORM	1,C�� 2,B��
    # """
    sql = """select count(*) from msg_user_mapping where  to_org_user_id='{to_org_user_id}' and to_user_id='{to_user_id}' and user_status={user_status} and platform ={platform};

        """.format(to_org_user_id=to_org_user_id, to_user_id=to_user_id, user_status=user_status, platform=platform)
    print(sql)
    result =GetData(sql=sql).result()
    return result

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
    result =GetData(sql=sql).results()
    return result

