from bs4 import BeautifulSoup
from bs4.element import Comment

str = '''
<title id='js_title'>我是BS4</title>
<div class='info' float='left'>welcome to BS4</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.baidu.com'></a>
    <strong><!--没用的注释--></strong>
</div>
'''

soup = BeautifulSoup(str, 'lxml')


print(soup.title)
print(soup.div)
print(soup.div.attrs)
print(soup.div.get('class'))
print(soup.div['float'])
print(soup.div.string)
print(soup.div.text)
# 处理注释
if type(soup.strong.string) == Comment:
    print(soup.strong.prettify())
else:
    print(soup.strong.text)


# 正则匹配
print('-----------find_all---------')
print(soup.find_all('title'))
print(soup.find_all(id='js_title'))
print(soup.find_all(class_='info'))
print(soup.find_all(attrs={'float':'left'}))
print(soup.find_all('div', attrs={'float':'left'}))

# css选择器
print('------------css-------------')
print(soup.select('title'))
print(soup.select('#js_title'))
print(soup.select('.info'))
print(soup.select('div span'))
print(soup.select('div > span'))
print(soup.select('div')[1].select('a'))