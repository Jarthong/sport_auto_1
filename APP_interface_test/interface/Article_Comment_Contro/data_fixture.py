#!/user/bin/python
#encoding:utf-8

#__auth__=='__hq__'

from db_fixture.login_token import *
from db_fixture.mysql_db import *
from db_fixture.common import *

class RandomVar:
    "常用随机变量字段，如name,age,sex,bir,phone,email"

    def random_char_upper(self, num=5):
        '随机5位大写'
        return str(''.join(random.sample(GlobalVar.CHAR_UPPER, num)))


    def random_num(self, start=0, end=99999):
        '随机1-9,取数'
        return random.randint(start, end - 1)




    def random_az(self):
        '随机选择字母a-z'
        return chr(random.randint(97,122))

    def random_phone(self):
        '随机选择号码'
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153",
                   "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))




    def timeTemp(self, i=0):
        return str(date.today() + timedelta(days=i))

    def date(self):
        year = strftime("%Y", localtime())
        mon = strftime("%m", localtime())
        day = strftime("%d", localtime())
        hour = strftime("%H", localtime())
        min = strftime("%M", localtime())
        sec = strftime("%S", localtime())
        timeTemp = [year, mon, day, hour, min, sec]

        now = strftime("%Y-%m-%d %H:%M:%S")
        return now, timeTemp


    def datetime_timestamp(dt):
        """
        传日期格式，'%Y-%m-%d %H:%M:%S'
        :return:
        """
        time.strptime(dt, '%Y-%m-%d %H:%M:%S')
        s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
        return int(s)

    def current_timestamp(self):
        timestamp_cur = int(time.time())*1000  # 系统当前时间戳
        return timestamp_cur

    def next_timestamp(self):
        timestamp_ne = int(time.time()+604800)*1000  # 往后七天的时间戳
        return timestamp_ne

    def random_idNum(self):
        """随机选择证件号码"""
        numlist = [440308198601013698, 440308198601019774, 440308198601019934, 440308198601010438, 440102199901010777,
             440102199901018218, 440102199901016458, 440102199901013935, 440102199901018752, 440103198501010198,
             440103198501019192, 440103198501014359, 440103198501017138, 440103198501018296, 440105199901018938,
             440105199901018938, 440105199901012691, 440105199901019279, 440105199901016457, '44010519990101745x',
             440306199901017959, 440306199901013050, '44030619990101263x', 440306199901013237]
        return random.choice(numlist)


class Article_Information(RandomVar):
    def __init__(self):
        self.getdb = DB()

    def article(self,PUBLISH_STATUS):
        """资讯表,PUBLISH_STATUS=0,未发布;1,已发布;2:发布失败;3,草稿'"""
        sql = "select * from article where PUBLISH_STATUS = {PUBLISH_STATUS} order by PUBLISH_TIME DESC limit 1,800;".format(PUBLISH_STATUS=PUBLISH_STATUS)
        article_info = self.getdb.query(sql)
        article_result = [results for results in article_info]
        index = self.random_num(0,len(article_result))
        ARTICLEID,USERID = (article_result[index]['article_id'],article_result[index]['user_id'])
        return ARTICLEID,USERID

    def article_comment(self,USER_ID=GlobalVar.USERIDS_YMM,IS_DEL=0):
        """资讯评论表"""
        sql = "select * from article_comment t where USER_ID = '{USER_ID}' and IS_DEL = {IS_DEL} order by create_time desc limit 1,800;".format(USER_ID=USER_ID,IS_DEL=IS_DEL)
        comment_info = self.getdb.query(sql)
        comment_result = [results for results in comment_info]
        index = self.random_num(0,len(comment_info))
        commentid = (comment_result[index]['comment_id'])
        return commentid

if __name__ == "__main__":
    bs = Article_Information()
    # print(bs.email())
    # print(bs.match_and_ip_sign_mapping())
    #bs.match_and_ip_sign_mapping()
    # print(GlobalVar.JOIN_REQUIRE)
    bs.article(1)


