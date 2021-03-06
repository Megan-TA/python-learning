
from lxml import etree
import requests
from fake_useragent import UserAgent
from random import randint
from time import sleep

base_url = 'http://www.maoyan.com'

headers = {
    'User-Agent': UserAgent().chrome
}

def get_html(url):
    # 请求随机睡眠（3-10s以内） 防止被机器识别
    sleep(randint(3, 10))
    response = requests.get(url, headers = headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_index(html):
    e = etree.HTML(html)
    all_url = e.xpath('//div[@class="channel-detail movie-item-title"]/a[@data-act="movies-click"]/@href')
    return [base_url + '{}'.format(url) for url in all_url]


def parse_info(html):
    e = etree.HTML(html)
    # 演员的值有重复
    actors = e.xpath('//li[@class="celebrity actor"]/div[@class="info"]/a[@class="name"]/text()')
    name = e.xpath('//div[@class="movie-brief-container"]/h3/text()')[0]
    types = e.xpath('//li[@class="ellipsis"][1]/text()')[0]

    actors = format_actors(actors)
    return {
        "name": name,
        "types": types,
        "actors": actors
    }

def format_actors(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip())

    return actor_set

def main():
    index_url = 'http://maoyan.com/films'
    html = get_html(index_url)
    moive_urls = parse_index(html)
    for url in moive_urls:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie)

main()


