# try...except 语句用来处理程序运行过程中的异常
# try:
#     person = {"name": "zhang"}
#     print(person['age'])
#     print(1 / 0)
#     file = open('abc.txt')
#     print(file.read())
#     file.close()
# except Exception as e:
#     print(e)
# except:
#     print('出错了')
# except (FileNotFoundError, ZeroDivisionError, KeyError) as e:  # 处理指定类型的错误
#     print(e)


age = input('请输入您的年龄：')
# if age.isdigit():
try:
    age = float(age)
except ValueError as e:
    print('年龄必须是数字')
else:
    if age >= 18:
        print('欢迎来到大冰的小屋')
    else:
        print('未满18岁，请过完你的18岁生日再来吧')
