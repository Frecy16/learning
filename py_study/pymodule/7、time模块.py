import time

print(time.time())  # 获取从 1970-01-01 00:00:00 UTC 到现在时间的秒数
print(time.strftime("%Y-%m-%d %H-%M-%S"))  # 按照指定格式输出时间
print(time.asctime((1, 1, 1, 1, 1, 1, 2, 147, -1)))  # Mon Apr 15 20:03:23 2019
print(time.ctime())  # Mon Apr 15 20:03:23 2019  传入秒数

print('hello')
time.sleep(2)  # 让时间暂停10秒钟
print('world')
