__author__ = "xiaoke"
import json
import pymysql


class OperationMysql:
    '''操作数据库的类'''

    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='le_study',
            charset='utf8',
            # 将字段的值也拿出来，比如name:xiaoke
            cursorclass=pymysql.cursors.DictCursor
        )
        # 游标
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        result = json.dumps(res)
        return result


if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("select * from web_user where Name='mushishi'")
    print(res)
