# 1、声明一个字典，保存用户的姓名、年龄、成绩、电话、性别
# student = {'name': '张三', 'age': 18, 'score': 98, 'tel': '13800000001', 'gender': 'male'}

# 2. 声明一个列表，在列表中保存6个学生的信息

students = [
    {'name': '李四', 'age': 18, 'score': 98, 'tel': '13800000001', 'gender': 'female'},
    {'name': '王五', 'age': 28, 'score': 79, 'tel': '13888888881', 'gender': 'male'},
    {'name': '刘敏', 'age': 21, 'score': 88, 'tel': '13888888888', 'gender': 'unknown'},
    {'name': 'chars', 'age': 15, 'score': 58, 'tel': '13800001002', 'gender': 'unknown'},
    {'name': 'jack', 'age': 23, 'score': 56, 'tel': '13800001003', 'gender': 'female'},
    {'name': 'tony', 'age': 17, 'score': 98, 'tel': '13800001008', 'gender': 'unknown'}
]

# (1) 统计不及格学生的个数
# count = 0
# for stu in students:
#     if stu['score'] < 60:
#         count +=1
# print('不及格的学生有{}个'.format(count))

# (2) 打印不及格学生的名字和对应的成绩
# for stu in students:
#     if stu['score'] < 60:
#         print(stu['name'],stu['score'])

# (3) 统计未成年学生的个数
# teenager_count = 0
# for stu in students:
#     if stu['age'] < 18:
#         teenager_count += 1
# print('未成年的学生有{}人'.format(teenager_count))

# (4) 打印手机尾号为8的学生的名字
# for stu in students:
#     if stu['tel'][-1] == '8':
#         print(stu['name'])

# (5) 打印最高分和对应的学生姓名
# n = 0
# max_score = students[0]['score']
# while n < len(students):
#     if students[n]['score'] > max_score:
#         max_score = students[n]['score']
#     n += 1
# for stu in students:
#     if stu['score'] == max_score:
#         print(stu['name'])

# (6) 删除性别不明的所有学生
# i = 0
# while i < len(students):
#     if students[i]['gender'] == 'unknown':
#         students.pop(i)
#         i -= 1
#     i += 1
# print(students)

# for stu in students[:]:
#     if stu['gender'] == 'unknown':
#         students.remove(stu)
# print(students)

# (7) 将列表按学生成绩从大到小排序
for j in range(len(students) - 1):
    for i in range(len(students) - 1 - j):
        if students[i]['score'] < students[i + 1]['score']:
            students[i], students[i + 1] = students[i + 1], students[i]
print(students)
