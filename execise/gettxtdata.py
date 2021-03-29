import pandas as pd

data = pd.read_json('C:/Users/frecy/Desktop/prodata/trade2.json')
# print(data["data"]["records"])
count = 1
orderSnFile = open('C:/Users/frecy/Desktop/orderSn.txt', 'a')
for i in data["data"]["records"]:
    print(i["orderSn"])
    orderSnFile.write(i["orderSn"] + '\n')
    count += 1
print(count)
orderSnFile.close()
