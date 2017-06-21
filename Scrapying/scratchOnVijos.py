from bs4 import BeautifulSoup
from Scrapying.request_url import getcode
import re


url_origin = 'https://vijos.org'


def get_task_url(internal_url):
    """
    :param internal_url:  VIJOS 的内链
    :return: 对应的网址
    """
    return url_origin + internal_url


def get_vijos_tasks():
    """
    :return: list task_urls shows that task in it
    """
    task_urls = []
    url_tosearch = 'https://vijos.org/d/tongji_sse_2016_cpp/p'
    t = getcode(url_tosearch)
    bs = BeautifulSoup(t, 'html.parser')
    for link in bs.find_all('td', {'class': 'col--name col--problem-name'}):
        for s in link.find_all('a'):
            if 'href' in s.attrs:
                task_urls.append(get_task_url(s['href']))
    return task_urls


def get_to_submit(question_url):
    """
    :param question_url: the url of the question like  
    'https://vijos.org/d/tongji_sse_2016_cpp/p/5921ae62d3d8a17e55ed66af'
    :return: 
    """
    text = getcode(question_url)
    bsObj = BeautifulSoup(text, 'html.parser')
    find_it = False
    for link in bsObj.findAll('dl'):
        for child_link in link.children:
            if child_link.string == '\n':
                continue
            if find_it:
                bs_final = BeautifulSoup(str(child_link), 'html.parser')
                return 'https://vijos.org' + bs_final.find('a')['href']
            if child_link.text == '递交数':
                find_it = True


def load_student_data(student_info_url):
    """
    :param student_info_url: the url of student  
    :return: a list shows 'solved' 'rp' 'number'(0, 1, 2)
    """
    text = getcode(student_info_url)
    bs_per_user = BeautifulSoup(text, 'html.parser')
    for message in bs_per_user.findAll('div', {'class': 'media__body profile-header__main'}):
        message_bs = BeautifulSoup(str(message), 'html.parser')
        s = message_bs.findAll('p')[1].string
        # 解决了 1 道题目，RP: 57.5 (No. 68)
        # 数字 表示solved rp number(l[0], 1, 2)
        l = re.findall('\d+[.\d+]*', s)
        return l


chara_pre_url = 'https://vijos.org/d/tongji_sse_2016_cpp/user/'
test_url = '/d/tongji_sse_2016_cpp/records?pid=5921ae62d3d8a17e55ed66af'


def get_per_url(chara):
    """
    :param chara: the member of users (student name, student index)
    :return: the real url of the 
    """
    return chara_pre_url + chara[1]


def get_user_sets(problem_url):
    """
    :param problem_url: the internal link of the url of the problem 
    :return: a set of users of (student name, student index)
    """
    users = set()
    problem_attr = 'col--problem col--problem-name'
    text = getcode(problem_url)
    bs_page = BeautifulSoup(text, 'html.parser')
    for link_user in bs_page.findAll('a', {'href': re.compile(r'\w+/user/\d+')}):
        name = link_user.string
        index = link_user['href'][-6:]
        if (name, index) not in users:
            users.add((name, index))
    return users
