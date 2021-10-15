import redis

client = redis.Redis(host='192.168.61.130', port='6379')

print(client.get('name1'))
print(client.hget('dog', 'name'))
print(client.hgetall('dog'))
print(client.lrange('sanguo', 0, -1))
print(client.srandmember('shiren'))
print(client.smembers('shiren'))
print(client.zrange('xiyouji', 0, 100))
