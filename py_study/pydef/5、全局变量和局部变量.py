a = 100  # 这个变量是全局变量，在整个py文件里都可以访问
word = 'butiful'


def Test():
    x = 'hello'  # 在函数内部定义的变量，它是局部变量，只能在函数内部使用
    print('x = {}'.format(x))
    # print('函数内部 a = {}'.format(a))

    # 如果局部变量的名和全局变量同名，会在函数内部又定义一个新的局部变量
    a = 10  # 在函数内部又定义了一个新的局部变量
    print('函数内部 a = {}'.format(a))

    # 函数内部如果想要修改全部变量
    global word
    word = 'ok'

    print('locals = {}, globals = {}'.format(locals(), globals()))


Test()
print('函数外部 a = {}'.format(a))
print('函数外部 word = {}'.format(word))

# 内置函数 globals()可以查看全局变量  locals() 可以查看局部变量
# 在Python里，只有函数能够分割作用域

if 3 > 2:
    m = 'test'  # 条件成立时,m是全局变量，条件不成立，m未定义
print(m)
