"""
房子（House）有户型、总面积、剩余面积 和 家具名称列表 属性
新房子没有任何的家具
将 家具的名称 追加到 家具名称列表 中
判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加这件家具

家具（Furniture） 有 名字 和 占地面积 属性，其中
席梦思（bed） 占地 4 平米
衣柜（chest） 占地 2 平米
餐桌（table） 占地 1.5 平米
将以上三件 家具 添加 到 房子 中
打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
"""


class House(object):
    def __init__(self, house_type, total_area, fur_list=None):
        if fur_list is None:  # 如果值是None
            fur_list = []  # 将fur_list设置为空列表
        self.house_type = house_type
        self.total_area = total_area
        self.fur_list = fur_list
        self.free_area = total_area * 0.6

    def add_fur(self, fur):
        if fur.area < self.free_area:
            self.fur_list.append(fur.name)
            self.free_area -= fur.area
        else:
            print(f'房子剩余空间不够了，不能添加 "{fur.name}" 这个家具了')

    def __str__(self):
        return '户型：{}，总面积：{} 平米，剩余面积：{:.2f} 平米，家具名称列表：{}'.format(self.house_type, self.total_area,
                                                                 self.free_area, self.fur_list)


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


if __name__ == '__main__':
    # 创建房间对象的时候，传入户型和总面积
    house = House('三室一厅', 116)
    bed = Furniture('席梦思', 4)
    chest = Furniture('衣柜', 2)
    table = Furniture('餐桌', 1.5)
    plane = Furniture('飞机', 100)

    # 把家具添加到房间里（面向对象关注点：让谁做）
    house.add_fur(bed)
    house.add_fur(chest)
    house.add_fur(table)
    house.add_fur(plane)
    print(house)  # print打印一个对象的时候，会调用这个对象的__repr__或者__str__方法，获取它们的返回值
    # print(house.__str__())  # 相当于print(house)
