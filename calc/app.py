from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/math/<arith>")
def math(arith):
    a = request.args["a"]
    b = request.args["b"]
    if arith == "add":
        return f"<h1>{int(a)+int(b)}</h1>"
    if arith == "sub":
        return f"<h1>{int(a)-int(b)}</h1>"
    if arith == "mult":
        return f"<h1>{int(a)*int(b)}</h1>"
    if arith == "div":
        return f"<h1>{int(a)/int(b)}</h1>"
