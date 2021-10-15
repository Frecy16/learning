# 1、判断用户输入的内容是否是数字，如果是数字转换成为数字类型
import re

# s = input('请输入一串数字：')
# if re.fullmatch(r'-?\d+(\.\d+)?$', s):
#     print(float(s))
# else:
#     print('输入的不是一个数字')


# 2.用户名：以非数字开头，后面由 字母 数字 _ - 组成的长度4 到 14位的字符串
# name = input('请输入：')
# if re.match(r'^\D[a-z0-9A-Z_\-]{3,13}', name):
#     print(name)
# else:
#     print('输入不符合规范')


# 3.匹配邮箱
# mail = input('请输入：')
# if re.match(r'^([a-zA-Z0-9_\-.])+@([a-z0-9A-Z_\-.])+\.[a-zA-Z]{2,4}$', mail):
#     print(mail)
# else:
#     print('输入不符合规范')

# 4.匹配手机号
# phone = input('请输入：')
# if re.match(r'^1[0-9]{10}$', phone):
#     print(phone)
# else:
#     print('输入不符合规范')

# # 5.匹配身份证号
# idCardNo = input('请输入：')
# if re.match(r'^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$', idCardNo):
#     print(idCardNo)
# else:
#     print('输入不符合规范')

# 6.匹配URL地址

# 7.匹配QQ号
# qq = input('请输入：')
# if re.match(r'^[1-9][0-9]{4,10}$', qq):
#     print(qq)
# else:
#     print('输入不符合规范')

# 8.匹配微信号
# vx = input('请输入：')
# if re.match(r'^[a-zA-Z]([a-zA-Z0-9_-]{5,19})+$', vx):
#     print(vx)
# else:
#     print('输入不符合规范')

# 9.匹配车牌号
carNo = input('车牌：')
result = re.match(r'^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼史领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$', carNo)
print(result)
