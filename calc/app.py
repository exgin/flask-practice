from flask import Flask, request
import operations


app = Flask(__name__)


@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = operations.add(a, b)

    return str(res)


@app.route('/subtract')
def subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = operations.sub(a, b)

    return str(res)


@app.route('/multiply')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = operations.mult(a, b)

    return str(res)


@app.route('/divide')
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = operations.div(a, b)

    return str(res)


MATH = {
    "add": add,
    "sub": subtract,
    "mult": multiply,
    "div": divide
}


@app.route('/math/<operations>')
def math(operations):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = MATH[operations](a, b)

    return str(res)
