import flask

# 服务器获取get发送的数据，服务器用flask中的request对象的args来存储get的参数
# flask.request.args.get(参数）用来获取参数的值。

app = flask.Flask(__name__)


@app.route("/")
def index():
    try:
        # 改进后 province和city没有出现在flask.request.args中时 将其设置为 空字符串
        province = flask.request.args.get("province") if "province" in flask.request.args else ""
        city = flask.request.args.get("city") if "city" in flask.request.args else ""
        return province + "," + city
    except Exception as err:
        return str(err)


if __name__ == "__main__":
    app.run()
