import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql

url = "http://datachart.500.com/ssq/"
headers = {
    "User-Agent": UserAgent().chrome
}

response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
# 期号集合
date_times = e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class)]')

# 连接数据库
client = pymysql.connect(host='localhost', port=3306, user='root', password='12345678', db='doubleball')
cursor = client.cursor()
sql = 'insert into t_ball values(0, %s, %s, %s)'
# 查看数据是否存在 防止重复值插入
index = 0
select_new_sql = 'select * from t_ball where date_time = %s'
for date_time in date_times:
    # 不存在返回0 存在返回1
    result = cursor.execute(select_new_sql, [date_time])
    if result == 1:
        break
    index += 1


for i in range(index):
    # 在之前查询的基础上查询使用 ./
    red_balls = '-'.join(trs[i].xpath('./td[@class="chartBall01"]/text()'))
    blue_balls = trs[i].xpath('./td[@class="chartBall02"]/text()')[0]
    cursor.execute(sql, [date_times[i], red_balls, blue_balls])
    client.commit()
    print('第' + date_times[i] + '：红球有' + red_balls + '，蓝球有' + blue_balls)

cursor.close()
client.close()
