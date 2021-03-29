# 用三个元组便是三门学科的选课学生姓名（一个学生可以同时选多门课）
# （1）求选课学生总共有多少人
# （2）求只选了第一个学科的人的数量和对应的名字
# （3）求只选了一门学科的学生的数量和对应的名字
# （4）求只选了两门学科的学生的数量和对应的名字
# （5）求选了三门学科的学生的数量和对应的名字

sing = ('李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石')
dance = ('李商隐', '杜甫', '李白', '白居易', '岑参', '王昌龄')
rap = ('李清照', '刘禹锡', '岑参', '王昌龄', '苏轼', '王维', '李白')

# 第(1)题：
# x = len(set(sing + dance + rap))
# print(x)

# 第(2)题：
# i = 0
# for stu in sing:
#     if stu not in dance and stu not in rap:
#         print(stu, end=' ')
#         i += 1
# print()
# print('只选择第一个学科的学生有 {} 人'.format(i))

# 第（3）题：
# sing_only = []
# total = sing + dance + rap
# for j in set(total):
#     if total.count(j) == 1:
#         sing_only.append(j)
# print('只选择一门学科的学生的有{}, 他们是{}'.format(len(sing_only), sing_only))

# 第（4）题：
# two_subject = []
# for n in set(total):
#     if total.count(n) == 2:
#         two_subject.append(n)
# print('只选择两门学科的学生的有{}, 他们是{}'.format(len(two_subject), two_subject))

# 第（5）题：
m = 0
for stu in sing:
    if stu in dance and stu in rap:
        print(stu, end=' ')
        m += 1
print()
print('选择三门学科的学生有 {} 人'.format(m))
