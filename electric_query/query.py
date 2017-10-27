from random import randint
import requests
from bs4 import BeautifulSoup

WEB_ATTRS = ('drlouming', 'drceng', 'dr_ceng', 'drfangjian')
ASK = ('校区？', '楼号', '楼层', '房间')
URL = 'http://202.120.163.129:88/'


def get_select(index: int, bs: BeautifulSoup):
    # select 标签
    select: BeautifulSoup = bs.find_all('select')[index]
    # l = [(i, i + 1) for i in range(10)]
    ops = select.find_all('option')
    # print(ops[1].attrs)
    # 是ATTRS, 而且是一个字典
    # 得到记录(表名称:实际内容)
    options = [(s.text.strip(), s.attrs['value']) for s in select.find_all('option') if s.attrs['value'] != '']
    # 多个元素要打包成元组
    for i, (name, _) in enumerate(options):
        print('{}. {}'.format(i, name))

    # 与IO交互, 记住TRY CATCH
    while True:
        try:

            choose = int(input('输入你想要的{}>>>'.format(ASK[index])))
            if choose >= len(options) or choose < 0:
                raise ValueError()
        except ValueError:
            print('Please input an value for {} to {}'.format(0, len(options) - 1))
        else:
            break

    choosed = options[choose][1] # 被选中的字
    return choosed


def get_view_state(req:requests):
    """
    :param req: return of a post request
    :return: the new view state
    """
    if isinstance(req, requests.models.Response):
        bs = BeautifulSoup(req.text, 'html.parser')
    else:
        bs = req
    return bs.find('div').find('input', {'name': "__VIEWSTATE"}).attrs['value']


def final_get(h5):
    bs = BeautifulSoup(h5, 'html.parser')
    span = bs.find('span')
    return span.text


kv = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0',
    'accept-encoding': 'gzip, deflate, br'
}

# 最初的请求正文
body = {
    # 'drlouming': 7,
    '__VIEWSTATEGENERATOR': 'CA0B0334',
    # '__EVENTTARGET': 'drlouming',
}


def excute_request(index: int, req: requests):
    bs = BeautifulSoup(req.text, 'html.parser')
    body['__VIEWSTATE'] = get_view_state(bs)
    body[WEB_ATTRS[index]] = get_select(index, bs)
    if index == 3:
        # index == 3, 处理其他标签
        body['ImageButton1.x'] = randint(5, 10)
        body['ImageButton1.y'] = randint(10, 20)
        body['radio'] = 'buyR'


def excute():
    session = requests.session()
    session.headers = kv
    for i in range(4):
        req = session.post(URL, body)
        excute_request(i, req)
    req = session.post(URL, body) # finally
    print(final_get(req.text))
    # print(req.text)


if __name__ == '__main__':
    # test_view_state()
    # main()
    # get_final()
    # with open('final.html', 'r') as f:
    #     get_select(1, BeautifulSoup(f.read(), 'html.parser'))
    excute()
