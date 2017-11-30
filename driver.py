"""
尝试使用WEBDRIVER

本来想用PROXY的，结果傻逼搞了半晚上，我应该加一个TODO让自己拿自己的SOCKS5干他妈的的...
https://tieba.baidu.com/p/5331473555
不管怎样，感谢贴吧老哥...
"""
from __future__ import absolute_import
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

import time


class Spider:
    DCAP = dict(DesiredCapabilities.PHANTOMJS)
    DCAP['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0'

    SERVICE_ARGS = [
        '--proxy=119.53.185.220:9000',
        '--proxy-type=https',
    ]

    TEST_URL = 'https://www.pixiv.net'

    def __init__(self):
        """
        initialize driver
        """
        self.driver = webdriver.PhantomJS(
            '/Users/fuasahi/Desktop/Python/phantomjs-2.1.1-macosx/bin/phantomjs',
            desired_capabilities=Spider.DCAP,
            # service_args=Spider.SERVICE_ARGS
        )

        # set cookie
        # self.driver.get('https://www.pixiv.net/')
        self.driver.get(Spider.TEST_URL)

        print('Start Sleep')
        time.sleep(10)

        with open('t1.html', 'w', encoding='utf-8') as f1:
            f1.write(self.driver.page_source)

        print('Well, initialized')

        self.driver.delete_all_cookies()

        from pixiv_cookie import cookies
        for cookie in cookies:
            if cookie['domain'] != '.pixiv.net':
                continue
            self.driver.add_cookie({k: cookie[k] for k in ('domain', 'name', 'value', 'path', 'expires') if k in cookie})

        print('Well, Cookie reseted')
        # self.driver.get('https://www.pixiv.net/')
        self.driver.get(Spider.TEST_URL)
        # print(self.driver.find_element_by_id('db-global-nav').text)
        print('Hey, Here we get it~')

    def search(self, search_name, pages):
        pass

    def show_status(self):
        """
        :return: source code of the page
        """
        return self.driver.page_source


if __name__ == '__main__':
    spd = Spider()
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(spd.show_status())

