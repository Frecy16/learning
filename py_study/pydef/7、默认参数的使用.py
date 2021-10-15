# def say_hello(city='北京', name, age):  # 缺省参数要放在后面
def say_hello(name, age, city='北京'):
    print('大家好，我是{}，我今年{}岁了，我来自{}'.format(name, age, city))


say_hello('李明', 18, '哈尔滨')  # 直接传递的参数叫做位置参数
say_hello('刘星', 19)
say_hello(age=15, name='查理', city='南京')  # 使用变量赋值传递的参数叫关键字参数
# 可以直接传递单个参数，也可以使用变量赋值的形式传参
# 如果有位置参数和关键字参数，关键字参数一定要放在位置参数的后面
say_hello('姚晨', age=15, city='南京')  # 如果传递参数，就使用传递的实参
# say_hello(name='鲁滨逊', 21, city='成都')  # 不能这样写
# 缺省参数：
# 有些函数的参数值，如果你传递了参数，就是用传递的参数
# 如果没有传递参数，就使用默认的值
# 缺省参数要放在后面

# print函数里end就是一个缺省参数
print('hello', '你好', sep='--', end='')
