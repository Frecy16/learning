"""
学生类Student:
    属性：学号，姓名，年龄，性别，成绩
班级类Grade:
    属性：班级名称，班级中的学生 【使用列表存储学生】
    方法：
        1.查看该班级中的所有学生的信息
        2.查看指定学号的学生信息
        3.查看班级中成绩不及格的学生信息
        4.将班级中的学生按照成绩降序排序
"""


class Student(object):
    def __init__(self, num, name, age, gender, score):
        self.num = num
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        return '学号：{}，姓名：{}，年龄：{}，性别：{}，成绩：{}'.format(self.num, self.name, self.age, self.gender, self.score)


class Grade(object):
    def __init__(self, name, stu_list=None):
        if stu_list is None:
            stu_list = []
        self.name = name
        self.stu_list = stu_list

    def get_student(self):
        if len(self.stu_list) == 0:
            print(self.name + '这个班级里还没有学生')
        else:
            print('班级名称：{}，班级里有{}个学生，他们是'.format(self.name, len(self.stu_list)))
            for stu in self.stu_list:
                print(stu)

    def get_stuById(self, n):
        for stu in self.stu_list:
            if stu.id == n:
                return stu
        else:
            return '未找到学号为{}的学生'.format(n)

    def get_stuUnpass(self):
        if len(self.stu_list) != 0:
            # for stu in self.stu_list:
            #     if stu.score < 60:
            #         print(stu)
            result = filter(lambda student: student.score < 60, self.stu_list)
            for stu in result:
                print(stu)
        else:
            print(self.name + '班级里还没有学生')

    def order_by_score(self):
        if len(self.stu_list) != 0:
            self.stu_list.sort(key=lambda student: student.score, reverse=True)
            # sorted(self.stu_list, key=lambda s: s.score, reverse=True)
            return self.stu_list


s1 = Student('1204001', '李明', 16, '男', 88)
s2 = Student('1204002', '萧强', 15, '男', 60)
s3 = Student('1204008', '韩梅梅', 17, '女', 72)
s4 = Student('1204022', '王思锦', 16, '女', 58)

g = Grade('软件一班', [s1, s2, s3, s4])
g1 = Grade('软件二班')

# print(s1)
# g.get_student()
# print(g.get_stuById('1204008'))
# g.get_stuUnpass()
x = g.order_by_score()
for i in x:
    print(i)

# g1.get_student()
# print(g1.get_stuById('1204001'))
# g1.get_stuUnpass()
# y = g1.order_by_score()
# print(y)
