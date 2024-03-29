import multiprocessing

# 创建队列时，可以指定最大长度。默认值是0，表示不限
q = multiprocessing.Queue(5)

q.put('hello')
q.put('good')
q.put('yes')
q.put('ok')
q.put('hello')

# print(q.full())  # True
# q.put('how')  # 无法放进去
# 往队列里放置了 how
# block = True: 表示阻塞，如果队列已经满了，就等待
# timeout 超时，等待多久以后程序会出错，单位是秒
# q.put('her', block=True, timeout=1)
# q.put_nowait('her')  # 等价于 q.put('how', block=False)

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
q.get(block=True, timeout=3)
