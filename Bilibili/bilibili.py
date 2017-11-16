from collections import namedtuple

import requests
from bs4 import BeautifulSoup, NavigableString

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0'
}

# 动画基础链接
BANGUMI_BASE_URL = 'http://bangumi.bilibili.com/anime/'

Record = namedtuple('Record', ('title', 'played', 'follower', ))


def get_response(request_url: str):
    """
    :param request_url: 要发送 GET 请求的URL
    :return: 返回的响应对象
    """
    try:
        # 伪造 HTTP 首部的'user-agent' 使其更像是浏览器发出的请求
        response = requests.get(request_url, headers=HEADERS, timeout=2)
        # 如果没有正常获得响应，则抛出异常
        response.raise_for_status()
        return response
    except Exception as e:
        raise e


def get_message(bangumi_url: str):
    """
    :param bangumi_url: 番剧对应URL
    :return:
    """
    response_bgm = requests.get(bangumi_url)
    bs = BeautifulSoup(response_bgm.content, 'html.parser')
    # with open('final.html', 'w') as f:
    #     f.write(response_bgm.text)
    # print(bs.find('h1', class_='info-title').content)
    bs_child: BeautifulSoup = bs.find('div', class_='info-count')
    # print(bs_child)
    index = 0
    record = []
    for bs_node in bs_child.children:
        if not isinstance(bs_node, NavigableString):
            # Bs用TEXT
            # print('{} :{}'.format(bs_node.find('span').text, ))
            record.append(bs_node.find('em').text)
            index += 1
        if index == 2:
            break
    return record


def cmp(record):
    to_cmp = record.follower
    # if to_cmp.find('万') == len(to_cmp):
    if '万' in to_cmp:
        return float(to_cmp.strip('万')) * 10000
    else:
        return float(to_cmp)


def fun():
    response: requests.Response = requests.get('http://bangumi.bilibili.com/web_api/timeline_global')
    # with open('bilibili.json', 'r') as f:
    # l = response.json()
    # print(l['result'])
    records = []
    recorded_title = set()

    for result in response.json()['result']:
        for season in result['seasons']:
            title = season['title']
            if title in recorded_title:
                continue
            recorded_title.add(title)
            season_id = season['season_id']
            # print(title)

            records.append(Record(title, *get_message(BANGUMI_BASE_URL + str(season_id))))

    records.sort(key=cmp, reverse=True)
    for anime in records:
        print('动画 {} 有 {} 的播放量, {} 的关注者'.format(
            anime.title,
            anime.played,
            anime.follower
        ))


if __name__ == '__main__':
    fun()
