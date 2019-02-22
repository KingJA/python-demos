from urllib import request

req = request.Request(
    "https://baike.baidu.com/item/%E7%AC%AC%E4%BA%8C%E6%AC%A1%E4%B8%96%E7%95%8C%E5%A4%A7%E6%88%98/174090?fromtitle=%E4%BA%8C%E6%88%98&fromid=497841&fr=aladdin")
req.add_header("User-Agent",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1")
repos = request.urlopen(req)
print(repos.read().decode("UTF-8"))
