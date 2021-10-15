import datetime as dt

# 以一个下划线 _ 开始
# 以两个下划线 __ 开始 __x
# 以两个下划线开始，再以下划线结束 __x__

# 涉及到四个类 datetime/date/time/timedelta
print(dt.datetime.now())  # 获取当前时间
print(dt.date(2020, 1, 1))  # 创建一个日期
print(dt.time(18, 23, 45))  # 创建一个时间
print(dt.datetime.now() + dt.timedelta(3))  # 计算三天以后的日期
