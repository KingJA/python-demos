import codecs
import re
import urllib.request
# from urllib import *
from urllib.request import *


# 获取html内容
def getHtml(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    data = data.replace("\n", "")
    return data

def saveData(html, page=1):
    # reg = r'class="w2 readContent" original-title=\'(.*?)\'>'
    reg = r'class="houseListTitle "> (.*?)\</a>'
    imgre = re.compile(reg)
    texts = re.findall(imgre, html)
    x = (page - 1) * 10
    f = codecs.open('data\\data.txt', 'a', 'utf-8')
    for text in texts:
        content = "#%d" % x + text + "\n"
        print(content)
        f.write(content)
        x += 1
    f.close()


print(getHtml("https://wenzhou.anjuke.com/sale/p1/?pi=baidu-cpc-wenzhou-tyong2&kwid=92110706642#filtersort"))

# for i in range(1, 1):
#     saveData(getHtml("https://wenzhou.anjuke.com/sale/p%d/?pi=baidu-cpc-wenzhou-tyong2&kwid=92110706642#filtersort" % i), i)