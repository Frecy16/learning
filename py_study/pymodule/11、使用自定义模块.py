# 一个模块本质上就是一个py文件
# 自己定义一个模块，其实就是自己写一个py文件
# 如果一个py文件想要当做一个模块被导入，文件名一定要遵守命名规范
# 必须由数字、字母或下划线组成，不能数字开头
# 导入了一个模块，就能使用这个模块里的变量和函数
# import my_mod

# 使用 from <module_name> import * 导入这个模块里"所有"的变量和函数
# 本质是读取模块里的 __all__ 属性，看这个属性里定义了哪些变量和函数
# 如果模块里没有定义 __all__ 才会导入所有不以 _ 开头的变量和函数
# 以一个下划线开头的变量，建议只在本模块里使用，别的模块不要导入
from my_mod import *

# print(my_mod.m)
# my_mod.test()

print(m)
test()
# print(n)  #  报错，通过from <module_name> import * 导入模块, __all__ 里没有n，不能使用

import my_mod

print(my_mod.n)  # 通过import导入，可以使用n

print(my_mod._age)  # 报错，_age在my_mod模块中已经被删除了，不能使用
