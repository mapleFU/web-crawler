from request_url import getcode
from bs4 import BeautifulSoup
import re

chara_pre_url = 'https://vijos.org/d/tongji_sse_2016_cpp/user/'


def get_per_url(chara):
    return chara[1] + chara_pre_url

users = set()
problem_attr = 'col--problem col--problem-name'
# users content: name
test_url = '/d/tongji_sse_2016_cpp/records?pid=5921ae62d3d8a17e55ed66af'
origin_url = 'https://vijos.org'
with open('test.html', 'r') as f:
    text = f.read()
    bs_page = BeautifulSoup(text, 'html.parser')
    for link_user in bs_page.findAll('a', {'href': re.compile(r'\w+/user/\d+')}):
        name = link_user.string
        index = link_user['href'][-6:]
        if (name, index) not in users:
            users.add((name, index))