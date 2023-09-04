import flask
app=flask.Flask(__name__) #前后都是两个下划线，注意大小写敏感

@app.route("/")
def hello():
    return "你好"

@app.route("/hi")
def hi():
    return "Hi,你好"

if __name__=="__main__":
    app.run()
