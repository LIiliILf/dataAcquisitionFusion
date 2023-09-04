import urllib.parse
import urllib.request

# get方法访问网站
# 客户端get方式发送数据，数据附加在url后面，加一个 ？ 然后数据之间用 & 隔开。

url = "http：//127.0.0.1：5000"
try:
    # 参数值包含汉字，使用urllib.parse.quote对参数值编码
    province = urllib.parse.quote("广东")
    city = urllib.parse.quote("深圳")
    data = "province=" + province + "&city=" + city
    resp = urllib.request.urlopen("http://127.0.0.1:5000?" + data)
    htmldata = resp.read()
    html = htmldata.decode()
    print(html)
except Exception as er:
    print(err)
