import requests
def getcode(text):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}       # 把信息的来源伪装成浏览器
        demo = requests.get(text, timeout=30, headers=kv)
        demo.raise_for_status() # 非200(正常访问, 引发异常)
        return demo.text
    except:
        return '产生异常'


def get_outer_links(pageUrl):
    pass_page = set()

    def getLinks():
        global pass_page
        if len(pass_page) <= 100:
            t = get_text(pageUrl)
            this_bs = BeautifulSoup(t, 'html.parser')
            for link in this_bs.find_all('a'):
                if 'href' in link.attrs:
                    geturl = link.attrs['href']
                    if geturl[:2] == '//':
                        geturl = urlparse(pageUrl).scheme +':'+ geturl
                    if geturl not in pass_page:
                        pass_page.add(geturl)
                        if len(pass_page) > 100:
                            return
                        getLinks(geturl)


def get_external_link(pageUrl):
    bs = BeautifulSoup(get_text(pageUrl), 'html.parser')
    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            pass