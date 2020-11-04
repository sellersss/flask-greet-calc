from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def func_add():
    """Adds a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a, b)

    return str(res)


@app.route("/sub")
def func_sub():
    """Subtracts a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = sub(a, b)

    return str(res)


@app.route("/mult")
def func_mult():
    """Multiplies a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = mult(a, b)

    return str(res)


@app.route("/div")
def func_div():
    """Divide a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = div(a, b)

    return str(res)


operations_view = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<ops>")
def func_math(ops):
    """Does math specified by a specific /math/ route"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = operations_view[ops](a, b)

    return str(res)