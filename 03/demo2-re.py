import re

str1 = 'I study Pytho3.7 everyday'

print('--------------match-------------------')
# 以下都是能匹配到第一个I的正则（一定从第一个字母开始匹配）
m1 = re.match(r'I', str1)
m2 = re.match(r'\w', str1)
m3 = re.match(r'.', str1)
m4 = re.match(r'\D', str1)
m5 = re.match(r'i', str1, re.I)
m6 = re.match(r'\S', str1)
m7 = re.match(r'study', str1) # 匹配不到
print(m5.group())

print('-----------search-----------------')
s1 = re.search(r'study', str1)
s2 = re.search(r'\w+y', str1)
s3 = re.search(r's\w+', str1)

print(s3.group())

print('-------findall------------')
f1 = re.findall(r'y', str1)

print(f1)


print('------------实践---------')
str2 = '<div><a href="http://www.baidu.com">我是Python3.7</a></div>'

t1 = re.findall(r'<a.+a>', str2)
print(t1)
t2 = re.findall(r'[\u4e00-\u9fa5]\w+\.\d', str2)
print(t2)
t3 = re.findall(r'<a href="(.+)"', str2)
print(t3)