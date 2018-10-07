# -*- coding: utf-8 -*-
import scrapy

# 携带cookie去登录
class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['sxt.cn']

    def start_requests(self):
        url = 'https://www.sxt.cn/index/user.html'
        cookie_str = 'acw_tc=7b39758815388788734911808e059c2e0521c0ab2ffd43ee475c5ae1857d57; PHPSESSID=ushkkuh66c2t21d8ace9unmbe5; UM_distinctid=1664c56f584126-0b6b3bcffdec82-346a7809-1aeaa0-1664c56f5857a5; CNZZDATA1261969808=948301094-1538878802-https%253A%252F%252Fwww.sxt.cn%252F%7C1538878802; NTKF_T2D_CLIENTID=guest299C0C41-CE9A-4286-0E61-4C56F5BC9903; nTalk_CACHE_DATA={uid:kf_10279_ISME9754_guest299C0C41-CE9A-42,tid:1538879059387095}; 53gid2=10628444874002; visitor_type=new; 53gid0=10628444874002; 53gid1=10628444874002; 53revisit=1538879059954; 53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_keyword=https%3A%2F%2Fwww.sxt.cn%2Findex%2Flogin%2Flogin.html; 53kf_72085067_land_page=https%253A%252F%252Fwww.sxt.cn%252Findex.html; kf_72085067_land_page_ok=1; nTalk_PAGE_MANAGE={|m|:[{|61503|:|790855|}],|t|:|10:24:45|}'
        cookies = {}
        for cookie_singeStr in cookie_str.split(';'):
            key, value = cookie_singeStr.split('=', 1)
            cookies[key.strip()] = value.strip()

        yield scrapy.Request(url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        print(response.text)
