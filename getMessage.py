from request_url import getcode
from bs4 import BeautifulSoup

test_url = 'https://vijos.org/d/tongji_sse_2016_cpp/user/117579'
with open('test.html', 'r') as f:
    text = f.read()
    bs_per_user = BeautifulSoup(text, 'html.parser')
    for message in bs_per_user.findAll('div', {'class': 'media__body profile-header__main'}):
        message_bs = BeautifulSoup(str(message), 'html.parser')
        s = message_bs.findAll('p')[1].string
        



