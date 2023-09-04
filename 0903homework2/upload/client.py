# web上传文件
# 启动服务器， client把文件发送到server
# 服务器获取拟上传的文件名称和数据，保存到服务器端
import urllib.request
import os  # python 标准库，实现基本操作系统交互功能

url = "http://127.0.0.1:5000/upload"
filePath = input("Enter the file:")
if os.path.exists(filePath):
    fobj = open(filePath, "rb")
    data = fobj.read()
    fobj.close()
    p = filePath.rfind('\\')
    # 找到path的最后一个‘\’的位置
    fileName = filePath[p + 1:]
    # 从最后一个‘\’的位置之后的一个位置截取出要下载的文件名称
    print("准备上传：" + fileName)
    # 客户端要上传二进制数据
    # 定义headers字典来指定设置表头content-type的值为 application/octet-stream，
    headers = {'content-type': 'application/octet-stream'}  # 字典，指明上传的文件类型
    purl = url + "?fileName=" + urllib.parse.quote(fileName)
    # 三个参数， 访问的网址；要上传的数据； 表头字典
    req = urllib.request.Request(purl, data, headers)  # 将表头加入到http请求中，合成一个Request对象req
    resp = urllib.request.urlopen(req)  # 传递request对象给服务器
    msg = resp.read().decode()  # 读取服务器的返回结果，是否成功的标签
    if msg == "OK":
        print("成功上传:", len(data), "字节")
    else:
        print(msg)
else:
    print("文件不存在!")
