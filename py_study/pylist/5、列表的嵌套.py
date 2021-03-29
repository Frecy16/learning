import random

# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
office = [[], [], []]
teacher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0
while i < len(teacher):
    r = random.choice(office)
    r.append(teacher[i])
    i += 1

print(office)
# 第0个房间有3个人，分别是
# 带下标一般都是用while
# 如果使用for循环，使用enumerate():
for i, room in enumerate(office):
    print('\n第{}个房间有{}个老师，分别是：'.format(i, len(room)), end='')
    for t in room:
        print(t, end='、')
