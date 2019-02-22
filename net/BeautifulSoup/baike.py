from bs4 import BeautifulSoup as bs
import re
from urllib.request import urlopen
import pymysql.cursors

# TODO 过滤出标签里有特殊属性的元素

htmlResult = urlopen(
    "https://baike.baidu.com/item/%E7%AC%AC%E4%BA%8C%E6%AC%A1%E4%B8%96%E7%95%8C%E5%A4%A7%E6%88%98/174090?fromtitle=%E4%"
    "BA%8C%E6%88%98&fromid=497841&fr=aladdin").read().decode("utf-8")

# print(htmlResult)
soup = bs(htmlResult, "html.parser")
items = soup.findAll("a", href=re.compile(r"^/item/"))
# print(items)

connect = pymysql.connect(host='localhost', user='root', password='wzy1gqqbuu', db='bdbk', charset='utf8mb4')

noRepeatList = []
for item in items:
    if item.string in noRepeatList:
        print("已经存在相同词条==========================================>")
        continue
    noRepeatList.append(item.string)
    print("词条：%s 链接：https://baike.baidu.com%s" % (item.string, item["href"]))

    # 获取会话指针
    cursor = connect.cursor()
    # 创建sql语句
    sql = "insert into `word`(`name`,`url`) value (%s,%s)"
    # 执行sql语句
    cursor.execute(sql, (item.get_text(), "https://baike.baidu.com" + item["href"]))
    # 提交
    connect.commit()
connect.close()
