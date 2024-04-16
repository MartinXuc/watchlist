from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/home")
def hello():
    return '欢迎来到我的watchlist'


@app.route("/user/<name>")
def user_page(name):
    return f"User:{escape(name)}"


@app.route("/test")
def test_url_for():
    print(url_for("hello"))
    print(url_for("user_page", name="greyli"))
    print(url_for("user_page", name="Xuchi"))
    print(url_for("test_url_for"))
    print(url_for('test_url_for', num=2))
    return "Test page"
