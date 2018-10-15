from redis import Redis
import json
import jieba


redis = Redis()
stopwords = set()
with open('', encoding='gbk') as f:
    for line in f:
        print(line.rstrip('\r\n').encode())
        stopwords.add(line.rstrip('\r\n'))
print(len(stopwords))
print(stopwords)
items = redis.lrange('dbreview:items', 0, -1)
print(type(items))


words = {}
for item in items:
    val = json.loads(item)['review']
    for word in jieba.cut(val):
        words[word] = words.get(word, 0) + 1
print(len(words))
print(sorted(words.items(), key=lambda x: x[1], reverse=True))