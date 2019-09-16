from bs4 import BeautifulSoup as bs
import re
from urllib.request import urlopen
import pymysql.cursors

htmlResult = urlopen(
    "https://www.zhongguofeng.com/maifangfengshui/list_1.html").read().decode("utf-8")

# print(htmlResult)
soup = bs(htmlResult, "html.parser")
# print(type(soup))
items = soup.findAll("div", class_="picbox")
noRepeatList = []
for item in items:
    a = item.contents[0]
    print(a.get('href'))
    for img in a.contents:
        print(img['alt'])
        print(img['src'])
    # print(type(a))
    # print(item.attrs['class'])
