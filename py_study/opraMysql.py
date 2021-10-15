import pymysql


class OperateMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.61.130',
            port=3306,
            user='cheny',
            passwd='123456',
            db='test1',
            charset='utf8',
        )
        self.cur = self.conn.cursor()

    def select(self, sql):
        self.cur.execute(sql)
        # result = self.cur.fetchone()
        result = self.cur.fetchall()
        return result

    def update(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            print("更新失败")
        self.conn.close()

    def insert(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            print("插入失败")
        self.conn.close()

    def delete(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            print("删除失败")
        self.conn.close()


if __name__ == '__main__':
    nm = input("请输入用户名：\n")
    sql = '''insert into user(username, sex, age, passwd) values('%s',  '男', 18, '123456')''' % nm
    sql1 = '''select username from user;'''
    # sql = sql%(nm)
    # OperateMysql().insert(sql)
    print(OperateMysql().select(sql1))
