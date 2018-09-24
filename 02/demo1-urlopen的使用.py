from urllib.request import urlopen

response = urlopen('https://www.cnblogs.com/it-tsz/p/9022456.html')

# 读取内容
info = response.read()

# 编码处理
result = info.decode()

print(result)

# 打印状态码
print(response.getcode())

# 打印真实url（处理重定向）
print(response.geturl())

# 打印响应头
print(response.info())