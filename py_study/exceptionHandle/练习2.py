"""
宠物店类 PetShop
属性：店名，店中的宠物 【使用列表存储宠物】
方法：展示所有宠物的信息

宠物狗类  PetDog
属性：昵称，性别，年龄，品种
方法：叫，拆家，吃饭

宠物猫类 PetCat
属性：昵称，性别，年龄，品种，眼睛的颜色
方法：叫，撒娇，吃饭
注意：狗的叫声是汪汪   猫的叫声是喵喵
狗吃的是骨头         猫吃的是鱼
"""


class PetShop(object):
    def __init__(self, name, pet_list=None):
        if pet_list is None:
            pet_list = []
        self.name = name
        self.pet_list = pet_list

    def show_pets(self):
        if len(self.pet_list) == 0:
            print('本店没有宠物')
        else:
            print('本店店名：{}， 本店有{}只宠物，分别是：'.format(self.name, len(self.pet_list)))
        for pet in self.pet_list:
            print(pet)


class Pet(object):
    def __init__(self, name, gender, age, breed):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed

    def __str__(self):
        return '名字：{}，性别：{}，年龄：{}，品种：{}'.format(self.name, self.gender, self.age, self.breed)

    def bark(self):
        print(self.name + '正在叫')

    def eat(self):
        print(self.name + '正在吃东西')


class PetDog(Pet):
    def bark(self):
        print(self.name + '在汪汪叫')

    def dealer(self):
        print(self.name + '正在拆家。。。')

    def eat(self):
        print(self.name + '正在啃骨头')


class PetCat(Pet):
    def __init__(self, name, gender, age, breed, eyes_color):
        super().__init__(name, gender, age, breed)
        self.eyes_color = eyes_color

    def __str__(self):
        x = super(PetCat, self).__str__()
        x += '，眼睛颜色：{}'.format(self.eyes_color)
        return x

    def bark(self):
        print(self.name + '正在喵喵叫')

    def coquetry(self):
        print(self.name + '正在撒娇')

    def eat(self):
        print(self.name + '正在吃鱼')


d1 = PetDog('二哈', '公的', 2, '哈士奇')
c1 = PetCat('团团', '母的', 1, '波斯猫', '黑色')

ph = PetShop('琪琪宠物店', [d1, c1])

d1.bark()
c1.coquetry()
ph.show_pets()
