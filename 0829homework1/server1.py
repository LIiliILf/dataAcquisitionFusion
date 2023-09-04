import flask

app = flask.Flask(__name__)


# 表示这个函数接收POST请求，要接收POST需要指明， 默认get
@app.route("/", methods=["POST"])
def index():
    try:
        # 服务器用 flask.request.form.get("参数")来获取参数的值
        province = flask.request.form.get("province") if "province" in flask.request.form else ""
        city = flask.request.form.get("city") if "city" in flask.request.form else ""
        return province + "," + city
    except Exception as err:
        return str(err)


if __name__ == "__main__":
    app.run()
