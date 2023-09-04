import urllib.request

url = "http://127.0.0.1:5000"
# urlopen是打开网站的函数，用于打开一个url网址的网站。
resp = urllib.request.urlopen(url)
data = resp.read()  # 把二进制数据html转为字符串，默认utf8
html = data.decode()
print(html)
