import random

dg = {"A": "GA", "B": "GB", "C": "GC", "D": "GD", "E": "GE"}

person = ['A', 'B', 'C', 'D', 'E']
gt = []
for g in dg.values():
    gt.append(g)
# print(gt)
random.shuffle(gt)
# print(gt)
for p in person:
    if dg[p] != gt[-1]:
        print('{}的礼物是{}'.format(p, gt[-1]))
        gt.remove(gt[-1])
    elif len(gt) != 1:
        print('{}的礼物是{}'.format(p, gt[-2]))
        gt.remove(gt[-2])
    else:
        print('本次分配不均，请重新分配')
