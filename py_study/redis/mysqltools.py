import pymysql

HOST = '192.168.61.130'
PORT = 3306
USER = 'cheny'
PASSWORD = '123456'


class MysqlConnect(object):
    @staticmethod
    def connect(sql):
        db = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            port=PORT,
            database='python201',
            charset='utf8')

        try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()
            cursor.close()
            # 关闭连接
            db.close()
            return result
        except Exception as e:
            return e


if __name__ == '__main__':
    r = MysqlConnect().connect("select * from emp where ename='smith';")
    print(r)
