from py_study.opraMysql import OperateMysql

usernm = input("请输入用户名：\n")
sex = ['男', '女']
names = []
sql = '''select username from user;'''
re = OperateMysql().select(sql)
for i in re:
    names.append(i[0])
print(names)

add_sql = '''insert into user(username, sex, age, passwd) values ('%s', '%s', "%s", '%s');'''

if usernm in names:
    print("用户名已存在")
else:
    pwd = input("请输入密码：\n")
    sex_id = int(input("请选择性别：1、男；2、女\n"))
    usersex = sex[sex_id - 1]
    age = input("请输入年龄：\n")
    OperateMysql().insert(add_sql % (usernm, usersex, age, pwd))

print(OperateMysql().select(sql))
