from lxml import etree

str = '''
<title id='js_title'>我是BS4</title>
<div class='info' float='left'>welcome to BS4</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.baidu.com'></a>
    <strong><!--没用的注释--></strong>
</div>
'''

res = etree.HTML(str)
texta1 = res.xpath('//div[2]/a')
print(texta1)
texta2 = res.xpath('//div[@class="info"]')
print(texta2)