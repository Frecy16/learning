import re

s = '你哦啊方hi ssdfsi LKj 开始发动机'
pha = []
# for i in s:
#     if ord(i) in range(65,91) or ord(i) in range(97,123):
#         pha.append(i)
# pha.sort()
# print(pha)

for j in s:
    if j.encode("utf8").isalpha():
        pha.append(j)
pha.sort()
print(pha)

# for m, n in enumerate(s):
#     print(m, n)

# r = re.findall(r'[a-zA-Z]', s)
# r.sort()
# print(r)
