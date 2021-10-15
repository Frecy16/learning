from pymongo import MongoClient

client = MongoClient(host='192.168.61.130', port=27017)

print(type(client))
db = client.python201
# db.student.insert_one({"name":"wangwei","age":30,"job":"poet"})
db.student.update({"age": 36}, {"name": "libai", "age": 36, "job": "poet"})

cursor1 = db.student.find()  # 获取到游标
for data in cursor1:
    print(data)
