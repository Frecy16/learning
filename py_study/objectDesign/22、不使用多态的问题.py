class PoliceDog(object):
    def attack_enemy(self):
        print('警犬正在攻击坏人')


class GuideDog(object):
    def lead_road(self):
        print('导盲犬正在领路')


class DetectionDog(object):
    def search_drug(self):
        print('缉毒犬正在搜索毒品')


class Person(object):
    def __init__(self, name):
        self.name = name
        self.dog = None

    def work_with_pd(self):
        self.dog.attack_enemy()

    def work_with_gd(self):
        self.dog.lead_road()

    def work_with_dd(self):
        self.dog.search_drug()


pd = PoliceDog()
gd = GuideDog()
dd = DetectionDog()
p1 = Person('张sir')
p1.dog = pd
p1.work_with_pd()

p1.dog = gd
p1.work_with_gd()

p1.dog = dd
p1.work_with_dd()
