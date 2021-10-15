# 系统内置的异常：
# ZeroDivisionError   # 除以0异常：1/0
# FileNotFoundError  # 文件不存在异常： open('xxx.txt)
# FileExistsError  # 多次创建同名的文件夹 os.mkdir('test')
# ValueError  # int('hello')
# KeyError  # person = {'name': 'zhangsan'}  person['age']
# SyntaxError  # print('hello', 'good')
# InderError  #  m = [1, 2, 3, 4]  m[6]
from myException import FormatError

passwd = input("请输入密码：")
m = 8
n = 20
if m <= len(passwd) <= n:
    print('密码符合规范')
else:
    # 使用 raise 关键字可以抛出一个异常
    raise FormatError(m, n)

print('将密码保存到数据库')
