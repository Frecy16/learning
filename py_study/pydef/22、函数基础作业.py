# 1、编写函数，求 1+2+3+...+N 的和
import random


def sumN(n):
    sn = 0
    for i in range(n + 1):
        sn += i
    return sn


def sumN1(n):
    if n == 0:
        return 0
    return sumN1(n - 1) + n


# 2、编写一个函数，求多个数中的最大值
def get_max(*args):
    x = args[0]
    for i in args:
        if i > x:
            x = i
    return x


# 3、编写一个函数，实现摇骰子的功能，打印N个骰子的点数和
def randNum(n):
    sn = 0
    for i in range(1, n + 1):
        m = random.randint(1, 6)
        # print(m)
        sn += m
    return sn


# 4、编写一个函数，交换指定字典的key和value
def exchangeDict(d1: dict):
    d2 = {}
    for k, v in d1.items():
        d2[v] = k
    return d2


# 5、编写一个函数，提取指定字符串中的所有字母，然后拼接在一起产生一个新的字符串
# 例如： 传入 '12a&bc12d-+'  -->  'abcd'
def newStr(s: str):
    s1 = ''
    for i in s:
        if i.encode('utf8').isalpha():
            s1 += i
    return s1


# 6、写一个函数，求多个数的平均值
def averageNum(*args):
    sn = 0
    for i in args:
        sn += i
    return sn / len(args)


# 7、写一个函数，默认求10的阶乘，也可以求其他数字的阶乘
def factor(n=10):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def factor1(n=10):
    if n == 0:
        return 1
    return factor(n - 1) * n


# ++++++++++++++++++注意：以下方法不能使用系统提供的相应的方法和函数，全部自己写++++++++++++++++
# 8、写一个自己的capitalize函数，能够将指定字符串的首字母变成大写字母
# 例如： 'abc' -> 'Abc'   '12asd' -> '12asd'
def my_capitalize(s: str):
    return s[0].upper() + s[1:]


# 9、写一个自己的endwith函数，判断一个字符串是否以指定的字符串结束
def my_isendwith(words, word):
    return words[-len(word):] == word


# 10、写一个自己的isdigit函数，判断一个字符串是否纯数字字符串
def my_isdigit(mystr):
    for i in mystr:
        if not '0' <= i <= '9':
            return False
    return True


# 11、写一个自己的upper 函数， 将一个字符串中所有的小写字母变成大写字母
# a-z ==> 97-123  A-Z ==> 65-91
def my_upper(mystr):
    s = ''
    for i in mystr:
        if 'a' <= i <= 'z':
            s += chr(ord(i) - 32)
        else:
            s += i
    return s


# 12、写一个自己的rjust函数，创建一个字符串的长度是指定长度，原字符串在新字符串中右对齐，剩下的部分用指定的字符填充
# 例如： 原字符：'abc'     宽度：7    字符：'^'   结果：'^^^^abc'
#       原字符：'你好吗'   宽度：5    字符：'0'   结果：'00你好吗'
def my_rjust(mystr, w, str1):
    if len(mystr) < w:
        return str1 * (w - len(mystr)) + mystr
    else:
        return mystr


# 13、写一个自己的index函数，统计到指定列表中指定元素的所有下标，如果列表中没有指定元素返回-1
def my_index(mylist, ele):
    l1 = []
    for k, v in enumerate(mylist):
        if v == ele:
            l1.append(k)
    if len(l1) == 0:
        return -1
    else:
        return l1


# 14、写一个自己的len函数，统计指定序列中元素的个数
def my_len(my_seq):
    j = 0
    for i in my_seq:
        j += 1
    return j


# 15、写一个函数实现自己in操作，判断指定序列中，指定的元素是否存在
def my_in(my_seq, str1):
    for i in my_seq:
        if i == str1:
            return True
    else:
        return False


# 16、写一个自己的replace函数，将指定字符中指定的旧字符串转换成指定的新字符串
def my_replace(my_str, old_str, new_str):
    s = ''
    i = 0
    while i < len(my_str):
        tmp = my_str[i:i + len(old_str)]
        if tmp != old_str:
            s += my_str[i]
            i += 1
        else:
            s += new_str
            i += len(old_str)
    return s


def my_replace1(my_str, old_str, new_str):
    l1 = my_str.split(old_str)
    s = new_str.join(l1)
    return s


# 17、写一个自己的max函数，获取指定序列中元素的最大值，如果序列是字典，取字典值的最大值
# 例如：序列：[-1, -12, -1, -9]   结果：-1
#      序列：'abcdpzasdz'        结果：'z'
#      序列：{'小明': 90, '张三': 76, '路飞': 30, '小花': 98}  结果：98
def my_max(my_seq):
    if type(my_seq) == dict:
        my_seq = list(my_seq.values())
    s = my_seq[0]
    for i in my_seq:
        if s < i:
            s = i
    return s


# 18、写四个函数，分别实现求两个列表的交集、并集、差集、补集的功能
# 交集
def list_unite(l1: list, l2: list):
    l3 = []
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3


# 并集
def list_union(l1: list, l2: list):
    return list(set(l1 + l2))


# 差集也叫补集
def list_diff(l1: list, l2: list):
    l3 = []
    for i in l1:
        if i not in l2:
            l3.append(i)
    return l3


def list_Symmetric_diff(l1: list, l2: list):
    l3 = []
    for i in l1 + l2:
        if (i in l1 and i not in l2) or (i in l2 and i not in l1):
            l3.append(i)
    return l3


if __name__ == '__main__':
    # print(sumN(10))
    # print(sumN1(10))
    # print(get_max(1, 3, 2, 2, 6))
    # print(randNum(2))
    # print(exchangeDict({'name': 'a', 'age': 18}))
    # print(newStr('2a&bc12d-+&Ss()000'))
    # print(newStr('好的2a&bc12d-+&Ss()000'))
    # print(averageNum(1, 3, 2, 2, 6))
    # print(factor1())
    # print(my_capitalize('abc'))
    # print(my_capitalize('12asd'))
    # print(my_isendwith('abc123hello', 'hello'))
    # print(my_isendwith('abc123hello', 'll'))
    # print(my_isdigit('123a90'))
    # print(my_isdigit('12390'))
    # print(my_upper('adcBSDF123mn好的'))
    # print(my_rjust('abc', 7, '^'))
    # print(my_rjust('你好吗', 5, '0'))
    # print(my_index([1, 2, 45, 'abc', 1, '你好', 1, 0], 1))
    # print(my_len('好好的123aadvc**'))
    # print(my_in((12, 90, 'abc'), '90'))
    # print(my_replace('hello', 'l', 'xa'))
    # print(my_replace('how1 you and yousdf fine you ok', 'you', 'me'))
    # print(my_replace1('hello', 'l', 'xa'))
    # print(my_max([-7, -12, -1, -9]))
    print(my_max({'小明': 90, '张三': 76, '路飞': 30, '小花': 98}))
