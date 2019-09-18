import urllib.request
import re
import time
from bs4 import BeautifulSoup as bs
import pymysql
from urllib import error
from bs4.element import NavigableString


class FengshuiLoader:
    # 初始化
    def __init__(self):
        self.pageIndex = 1
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
                        'Referer': 'https://www.zhongguofeng.com/'}  # 加Referer 模拟真实访问，防盗链
        self.conn = pymysql.connect(host='localhost', user='root', password='wzy1gqqbuu', database='fengshui')
        self.cursor = self.conn.cursor()

    # 获取html
    def getHtml(self, url):
        # url = "https://www.zhongguofeng.com/maifangfengshui/list_%d.html" % pageIndex
        # print(url)
        req = urllib.request.Request(url)
        # 插入head
        for i in self.headers:
            req.add_header(i, self.headers[i])
        html = ''
        try:
            html = urllib.request.urlopen(req).read().decode("utf8")
        except error.URLError as e:
            print('错误：', e.reason)
        return html

    def getPageHtml(self, detailUrl):
        url = 'https://www.zhongguofeng.com%s' % (detailUrl)
        print('开始爬取详情页>>>>:', url)
        req = urllib.request.Request(url)
        for i in self.headers:
            req.add_header(i, self.headers[i])
        html = urllib.request.urlopen(req).read().decode("utf8")
        return html

    # 获取所需数据-单线程
    def saveData(self, html, information_type):
        if html == '':
            return
        soup = bs(html, "html.parser")
        # print(type(soup))
        liItems = soup.findAll(name="li", attrs={'ot': 3})
        print('liItems', liItems)
        noRepeatList = []
        for li in liItems:
            thumb_url = li.contents[0].a.img['src']
            detailUrl = 'https://www.zhongguofeng.com%s' % (li.contents[0].a.get('href'))
            title = li.contents[1].div.b.a.string

            print("thumb_url", thumb_url)
            print("detailUrl", detailUrl)
            print("title", title)
            if detailUrl in noRepeatList:
                print("已经存在相同词条==========================================>")
                continue
            noRepeatList.append(detailUrl)
            contentHtml = self.getHtml(detailUrl)
            soup = bs(contentHtml, "html.parser")
            contentDiv = str(soup.find("div", class_="content"))
            print('contentDiv', contentDiv)
            # 保存到数据库
            sql = "insert into fs (title,thumb_url,content,tag ) values (%s, %s, %s, %s)"
            self.cursor.execute(sql, (title, thumb_url, contentDiv, information_type))
            self.conn.commit()
        return

    def start(self):
        print("开始爬取风水")
        time1 = time.time()
        # tagList = ['fengshuixue','yangzhaifengshui','jiajufengshui','','','','','','']
        # url = "https://www.zhongguofeng.com/%s/list_%d.html" % (pageIndex, pageIndex)
        # html = self.getHtml(111)
        # self.saveData(html)
        # for i in range(1):
        #     self.getData(self.getPageHtmlByIndex(i + 1))

        tagUrlMap = self.getTagUrlMap()
        print("tagUrlList1", tagUrlMap)
        for key, value in tagUrlMap.items():
            value = value.replace('@', '%d')
            index = 1
            newUrl = value % index
            print("newUrl", newUrl)
            while self.getHtml(newUrl) != '' and index == 1:
                self.saveData(self.getHtml(newUrl), key)
                index = index + 1
                newUrl = value % index

        print("tagUrlMap", tagUrlMap)
        time2 = time.time()
        print('单线程耗时 : ' + str(time2 - time1) + ' s')
        self.cursor.close()

    def getTagUrlMap(self):
        homeHtml = self.getHtml("https://www.zhongguofeng.com/fengshui/")
        soup = bs(homeHtml, "html.parser")
        contentDiv = soup.find("div", class_="xglm")
        # contentDivStr = str(soup.find("div", class_="xglm"))
        # print("contentDivStr", contentDivStr)
        aTagList = contentDiv.contents
        # print("aTagList", aTagList)
        urlList = []
        tagMap = {}
        for aTag in aTagList:
            if isinstance(aTag, NavigableString):
                continue
            href = "https://www.zhongguofeng.com%slist_@.html" % (aTag.get('href'))
            tagMap[aTag.string] = href
        # print("tagMap", tagMap)
        return tagMap

    # 获取所需数据-单线程
    def saveData2(self, html):
        if html == '':
            return
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
            contentDiv = str(soup.find("div", class_="content"))
            # print('contentDiv', contentDiv)

            # for img in a.contents:
            # print('alt',img['alt'])
            # print('src',img['src'])
            # 保存到数据库
            # sql = "insert into fs (title,url,content ) values (%s, %s, %s)"
            # self.cursor.execute(sql, (a.string, a.get('href'), contentDiv))
            # self.conn.commit()


baike = FengshuiLoader()
print(baike.start())
