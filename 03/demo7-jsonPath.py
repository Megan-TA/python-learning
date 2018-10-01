import json
from jsonpath import jsonpath 

str = '{"name":"盗梦空间"}'

print(type(str))
# json序列化
obj = json.loads(str)
print(type(obj))
print(obj)

# json 反序列化
str2 = json.dumps(obj, ensure_ascii=False)
print(str2)

# json反序列化后内容写入文件
json.dump(obj, open('movie.txt', 'w', encoding='utf-8'), ensure_ascii= False)

# json打开一个文件
str3 = json.load(open('movie.txt', encoding='utf-8'))
print(str3)

# jsonPath使用
test = '{"name":"盗梦空间", "date": "2018/10/01"}'
name = jsonpath(json.loads(test), '$..name')
print(name)