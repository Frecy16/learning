import csv

# csv文件的写入
file = open('stu1.csv', 'w', encoding='utf8', newline='')  # newline=''不换行
w = csv.writer(file)
# 写入多行
w.writerows(
    [
        ['name', 'age', 'score', 'city'],
        ['刘明', 20, 93, '重庆'],
        ['李行', 23, 90, '桂林']
    ]
)
# w.writerow(['刘明', 20, 93, '重庆'])  # 写入一行

file.close()

# csv文件的读取
file1 = open('stuinfo.csv', 'r', encoding='utf8', newline='')
r = csv.reader(file1)
for data in r:
    print(data)

file1.close()
