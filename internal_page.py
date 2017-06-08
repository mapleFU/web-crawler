from request_url import getcode
from bs4 import BeautifulSoup
url = 'https://vijos.org/d/tongji_sse_2016_cpp/p/5921ae62d3d8a17e55ed66af'
text = getcode(url)
bsObj = BeautifulSoup(text, 'html.parser')
find_it = False
for link in bsObj.findAll('dl'):
    for child_link in link.children:
        if child_link.string == '\n':
            continue
        if find_it:
            bs_final = BeautifulSoup(str(child_link), 'html.parser')
            print(bs_final.find('a')['href'])
            find_it = False
            break
        if child_link.text == '递交数':
            find_it = True
