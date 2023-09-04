# web下载文件,服务器向客户端发送文件名称和文件数据的过程。
# 启动服务器返回可下载的文件名称给客户端，客户端发送需要下载的文件名称给server，server获取文件名称并返回文件的数据到client
import flask
import os  # 磁盘文件管理库

app = flask.Flask(__name__)


@app.route("/")
def index():
    if "fileName" not in flask.request.values:
        return "图像.jpg"
    else:
        data = b""
        try:
            fileName = flask.request.values.get("fileName")
            # 如果再次访问服务器，并带上fileName的参数，那么服务器接收这个文件名称后就使用os.path.exists(fileName)判断这个文件是否存在，
            # 如果存在就读取该文件的数据返回给客户端，如果不存在就返回空值给客户端。
            if fileName != "" and os.path.exists(fileName):
                fobj = open(fileName, "rb")
                data = fobj.read()
                fobj.close()
        except Exception as err:
            data = str(err).encode()
        return data


if __name__ == "__main__":
    app.run()
