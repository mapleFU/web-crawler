from bs4 import BeautifulSoup
from request_url import getcode
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
    for link in task_urls:
        # TODO : fill this
        pass

