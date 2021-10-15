import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.61.130',
                     port=3306,
                     db='python201',
                     user='cheny',
                     passwd='123456')
# 创建游标对象
cursor = db.cursor()
# 数据列表
data = [('零基础学Python', 'Python', '79.80', '2018-5-20'),
        ('Python从入门到精通', 'Python', '69.80', '2018-6-18'),
        ('零基础学PHP', 'PHP', '69.80', '2017-5-21'),
        ('PHP项目开发实战入门', 'PHP', '79.80', '2016-5-21'),
        ('零基础学Java', 'Java', '69.80', '2017-5-21'), ]
try:
    # 执行sql语句，插入多条数据
    cursor.executemany('insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)', data)
    # 提交数据
    db.commit()
except Exception as e:
    # 发生错误时回滚
    db.rollback()
    print(e)

# 关闭数据库连接
db.close()
