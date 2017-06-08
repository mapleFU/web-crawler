from request_url import getcode
from bs4 import BeautifulSoup
url = 'https://vijos.org/d/tongji_sse_2016_cpp/p/5921ae62d3d8a17e55ed66af'
# print(getcode(url))
bsObj = BeautifulSoup(getcode(url), 'html.parser')
for link in bsObj.findAll('dt'):
    if link.text == '递交数':
        print(link.next_sibling)
    #     print(link.next_sibling.children['href'])
# print(bsObj)