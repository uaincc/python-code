#!/usr/bin/env/ python3

"""
爬虫可以按照指定的规则自动浏览或抓取网络中的数据信息，而通过 Python Requests 可以很轻松的编写爬虫程序或者脚本。

此代码抓取网站【https://uain.cc/】中的博客文章

数据格式
{"title":<文章标题>,"url":<文章链接>}

依赖模块
pip install requests
pip install lxml
"""

import requests
from lxml import etree


def get_url():
    ''' URL 地址 可以这里准备大量URL地址 以我的博客文章为例'''
    url = 'https://uain.cc/'
    url_list = []
    url_list.append(url)
    return url_list


def pares_url(url):
    ''' URL 解析'''
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36",
        }
    response = requests.get(url, headers=headers, timeout=5)
    # 解码
    response.encoding
    response.encoding ='UTF-8'
    return response.text


def get_content(response):
    ''' 提取数据'''
    content_list = []
    html = etree.HTML(response)
    # 提取文章列表
    elements = html.xpath('//*[@id="post_item"]')
    for element in elements:
        # 将文章以字典形式保存
        item = {}
        item['title'] = element.xpath('.//h2/a/text()')[0]
        item['url'] = 'https://uain.cc/' + element.xpath('.//h2/a/@href')[0]
        content_list.append(item)
    return content_list


def save_content(content):
    '''保存数据'''
    print(content)


def run():
    ''' 爬虫程序入口 '''
    for url in get_url():
        response = pares_url(url)
        content_list = get_content(response)
        save_content(content_list)


def main():
    run()


if __name__ == '__main__':
    main()
