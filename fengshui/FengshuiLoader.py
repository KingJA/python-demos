import urllib.request
import re
import time
from bs4 import BeautifulSoup as bs
import pymysql


class FengshuiLoader:
    # 初始化
    def __init__(self):
        self.pageIndex = 1
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
                        'Referer': 'https://www.zhongguofeng.com/maifangfengshui/'}  # 加Referer 模拟真实访问，防盗链
        self.conn = pymysql.connect(host='localhost', user='root', password='wzy1gqqbuu', database='fengshui')
        self.cursor = self.conn.cursor()

    # 获取html
    def getPageHtmlByIndex(self, pageIndex):
        url = "https://www.zhongguofeng.com/maifangfengshui/list_%d.html" % pageIndex
        print(url)
        req = urllib.request.Request(url)
        for i in self.headers:
            req.add_header(i, self.headers[i])
        html = urllib.request.urlopen(req).read().decode("utf8")
        return html

    def getPageHtml(self, url):
        url = 'https://www.zhongguofeng.com%s' % (url)
        print('开始爬取详情页>>>>:', url)
        req = urllib.request.Request(url)
        for i in self.headers:
            req.add_header(i, self.headers[i])
        html = urllib.request.urlopen(req).read().decode("utf8")
        return html

    # 获取所需数据-单线程
    def getData(self, html):
        soup = bs(html, "html.parser")
        # print(type(soup))
        items = soup.findAll("div", class_="ujTitle")
        noRepeatList = []
        for item in items:
            a = item.contents[0].contents[0]
            # print('a',a)
            print('href', a.get('href'))
            print('title', a.string)
            if item.string in noRepeatList:
                print("已经存在相同词条==========================================>")
                continue
            noRepeatList.append(item.string)
            contentHtml = self.getPageHtml(a.get('href'))
            soup = bs(contentHtml, "html.parser")
            contentDiv =str(soup.find("div", class_="content"))
            print('contentDiv', contentDiv)

            # for img in a.contents:
            # print('alt',img['alt'])
            # print('src',img['src'])
            sql = "insert into fs (title,url,content ) values (%s, %s, %s)"
            self.cursor.execute(sql, (a.string, a.get('href'), contentDiv))
            self.conn.commit()


    def start(self):
        print("开始爬取风水")
        time1 = time.time()
        for i in range(79):
            self.getData(self.getPageHtmlByIndex(i + 1))
        time2 = time.time()
        print('单线程耗时 : ' + str(time2 - time1) + ' s')
        self.cursor.close()


baike = FengshuiLoader()
print(baike.start())

