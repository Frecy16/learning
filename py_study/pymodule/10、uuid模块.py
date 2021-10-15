# uuid用来生成一个全局唯一id的模块
import uuid

# 基于MAC地址，时间戳，随机数来生成唯一的uuid，可以保证全球范围内的唯一性,比较耗时间，效率低
print(uuid.uuid1())  # 32个长度  每一个字符有16个选择 ，16**32
# print(uuid.uuid2())  # python中没有基于DCE的算法，所以python的uuid模块中没有uuid2这个方法

# uuid3 和 uuid5是使用传入的字符串根据指定的算法算出来的，是固定的
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'zhangsan'))  # 生成固定的uuid，算法 md5
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'zhangsan'))  # 生成固定的uuid，算法 sha1

# 通过伪随机数得到uuid，是有可能重复的
print(uuid.uuid4())  # 生成随机uuid，使用的最多,如邮箱激活链接
