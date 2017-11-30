"""
主要是想看一眼PIXIV
本来想用自己电脑上的SS访问...看来设置还是有问题？只好先改了HOST,回去请教老司机
见这里吧...
https://2heng.xin/2017/09/19/pixiv/
代理也用的是别人的...
http://www.gatherproxy.com/zh/
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# import socks

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0',
    'proxy': '127.0.0.1:1080'
}

PROXIES = {
    'http': '159.192.236.196:54314',
    'https': '159.192.236.196:54314'
}


def get_response_with_proxy(url):
    """
    :param url: url
    :return: response text
    """
    response = requests.get(url, headers=HEADERS, timeout=5, proxies=PROXIES)
    response.raise_for_status()
    return response.text


def analyze_per_page(LOWER_STAR, valid_list, bs_obj):

    all: BeautifulSoup = bs_obj.find('div', {'class': '_2xrGgcY'})
    for pic_bs in all.find_all('div', {'class': '_7IVJuWZ'}):
        count = pic_bs.find('a', {'class': '_ui-tooltip bookmark-count'})
        print(count.text)


def has_content(pixiv_bs)->bool:
    """
    :param pixiv_bs: 搜索的单页对象
    :return: 返回一个布尔类型的两
    """
    return True


def main():
    MAX_PAGE = 1
    LOWER_STAR = 45
    BASE_SEARCH_TAG = 'https://www.pixiv.net/search.php?s_mode=s_tag&word={search}'

    word = '少女終末旅行'
    BASE_SEARCH_TAG = BASE_SEARCH_TAG.format(search=word)
    BASE_SEARCH_PAGE = BASE_SEARCH_TAG + '&order=date_d&p={page}'
    # get first response

    # 单线程的垃圾
    valid_list = list()
    for page in range(1, MAX_PAGE + 1):
        text = get_response_with_proxy(BASE_SEARCH_PAGE.format(page=page))

        # bs = BeautifulSoup(text, 'html.parser')
        # if not has_content(bs):
        #     break
        # analyze_per_page(LOWER_STAR, valid_list, bs)


if __name__ == '__main__':
    main()
