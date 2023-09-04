import urllib.parse
import urllib.request

# 1.先不带参数访问 url ，服务器会返回一个可以下载的文件名称给客户端。
url = "http://127.0.0.1:5000"
try:
    html = urllib.request.urlopen(url)
    html = html.read()
    fileName = html.decode()  # 服务器返回可以下载的文件名称
    print("准备下载:" + fileName)
    # 2.客户端获取这个文件名称，再次访问这个网站
    # urlretrieve函数用于从服务器获取文件并保存到本地。从url的网站下载数据保存到本地的localFile文件中
    urllib.request.urlretrieve(url + "?fileName=" + urllib.parse.quote(fileName), "download" + fileName)

    print("下载完毕")
except Exception as err:
    print(err)
