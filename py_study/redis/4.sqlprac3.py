import pymysql

db = pymysql.connect(host='192.168.61.130',
                     port=3306,
                     db='python201',
                     user='cheny',
                     passwd='123456')
cursor = db.cursor()
# 打印 MySQL 中 books表图书的名称和价格
# sql = 'select name,price from books'
# 查询books表图书价格小于 70元并且为 2017年以后出版的所有图书
# sql = 'select name,price,publish_time from books where publish_time>="2017-01-01";'
# 删除books表所有分类为PHP的图书，删除完成后查看所有图书
del_sql = 'delete from books where category="PHP";'
cursor.execute(del_sql)
sql = 'select name,price from books;'
cursor.execute(sql)
r = cursor.fetchall()
for i in r:
    print('图书：《%s》，价格：￥%s元' % (i[0], i[1]))
    # print('图书：《%s》，价格：￥%s元，出版日期：%s' %(i[0], i[1], i[2]))

db.close()
