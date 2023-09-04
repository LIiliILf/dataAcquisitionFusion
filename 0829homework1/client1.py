import urllib.parse
import urllib.request

# 客户端post发送数据
# 与get类似，不同点: get的参数放在地址栏的后面， post的数据放在urlopen函数的data参数（必须为二进制数据）中
url = "http://127.0.0.1:5000"
try:
    province = urllib.parse.quote("广东")
    city = urllib.parse.quote("深圳")
    data = "province=" + province + "&city=" + city
    # 把data字符串按utf8编码转为二进制数据
    data = data.encode()
    html = urllib.request.urlopen("http://127.0.0.1:5000", data=data)  # data接收二进制数据
    html = html.read()
    html = html.decode()
    print(html)
except Exception as err:
    print(err)
