from urllib.request import Request
from urllib.request import urlopen
from urllib import parse

req = Request("http://www.wanandroid.com/user/login")
# req = Request("http://www.wanandroid.com")
req.add_header("User-Agent",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1")
postData = parse.urlencode([
    ("username", "dd"),
    ("password", "ff")])
repos = urlopen(req, data=postData.encode("utf-8"))
htmlResult = repos.read().decode("utf-8")
print(htmlResult)
