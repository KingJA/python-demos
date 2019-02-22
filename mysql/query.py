import pymysql.cursors

connect = pymysql.connect(host='localhost', user='root', password='wzy1gqqbuu', db='bdbk', charset='utf8mb4')

try:
    with connect.cursor() as cursor:
        sql = "select `url`,`name` from word"
        # 获取总数
        count = cursor.execute(sql)
        print(count)
        # 查询数据
        # allData = cursor.fetchall()
        # print(allData)
        # 查询指定数量数据
        allData = cursor.fetchmany(3)
        print(allData)
finally:
    connect.close()
