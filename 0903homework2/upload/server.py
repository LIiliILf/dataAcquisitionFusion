import flask

app = flask.Flask(__name__)

# 运行后等待客户端上传文件， 有文件上传就读取上传文件的名称和数据，存储在磁盘中。
@app.route("/upload",methods=["POST"])
def uploadFile():
    msg=""
    try:
        if "fileName" in flask.request.values:
            fileName = flask.request.values.get("fileName")#获取文件名称
            # 获取数据， 使用flask.request的get_data()函数读取二进制数据
            data=flask.request.get_data()#获取数据
            fobj=open("upload "+fileName,"wb")
            fobj.write(data)
            fobj.close()
            msg="OK"
        else:
            msg="没有按要求上传文件"
    except Exception as err:
        print(err)
        msg=str(err)
    return msg

if __name__ == "__main__":
    app.run()
