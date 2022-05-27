from db_fixture.common import RandomVar
from db_fixture.mysql_db import DB


class Article_Information():
    def __init__(self):
        self.getdb = DB()

    def article(self,PUBLISH_STATUS):
        """资讯表,PUBLISH_STATUS=0,未发布;1,已发布;2:发布失败;3,草稿'"""
        sql = "select * from article where PUBLISH_STATUS = {PUBLISH_STATUS} order by PUBLISH_TIME DESC limit 10;".format(PUBLISH_STATUS=PUBLISH_STATUS)
        article_info = self.getdb.query(sql)
        article_result = [results for results in article_info]
        index = RandomVar().random_num(0,len(article_result))
        ARTICLEID,USERID = (article_result[index]['ARTICLE_ID'],article_result[index]['USER_ID'])
        return ARTICLEID,USERID



if __name__ == "__main__":
    bs = Article_Information()
    # bs.article(1)
    # print(bs.article(1))
    print(bs)


