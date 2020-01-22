# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route("/add")
def adding_numbers():
    value1 = int(request.args.get("a"))
    value2 = int(request.args.get("b"))
    return f"{operations.add(value1, value2)}"

@app.route("/sub")
def subtrscting_numbers():
    value1 = int(request.args.get("a"))
    value2 = int(request.args.get("b"))
    return f"{operations.sub(value1, value2)}"

@app.route("/mult")
def multiplying_numbers():
    value1 = int(request.args.get("a"))
    value2 = int(request.args.get("b"))
    return f"{operations.mult(value1, value2)}"

@app.route("/div")
def dividing_numbers():
    value1 = int(request.args.get("a"))
    value2 = int(request.args.get("b"))
    return f"{operations.div(value1, value2)}"