# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


@app.route("/math/<operation>")
def math(operation):
    
    value1 = int(request.args.get("a"))
    value2 = int(request.args.get("b"))

    math_operations = {'add':operations.add(value1,value2), 'sub':operations.sub(value1,value2), 'mult':operations.mult(value1,value2), 'div':operations.div(value1,value2)}

    return str(math_operations[operation])

    # if operation == 'add':
    #     return f"{operations.add(value1, value2)}"
    # elif operation =='sub':
    #     return f"{operations.sub(value1, value2)}"
    # elif operation =='mult':
    #     return f"{operations.mult(value1, value2)}"
    # elif operation =='div':
    #     return f"{operations.div(value1, value2)}"




# def adding_numbers():
#     value1 = int(request.args.get("a"))
#     value2 = int(request.args.get("b"))
#     return f"{operations.add(value1, value2)}"

# @app.route("/sub")
# def subtrscting_numbers():
#     value1 = int(request.args.get("a"))
#     value2 = int(request.args.get("b"))
#     return f"{operations.sub(value1, value2)}"

# @app.route("/mult")
# def multiplying_numbers():
#     value1 = int(request.args.get("a"))
#     value2 = int(request.args.get("b"))
#     return f"{operations.mult(value1, value2)}"

# @app.route("/div")
# def dividing_numbers():
#     value1 = int(request.args.get("a"))
#     value2 = int(request.args.get("b"))
#     return f"{operations.div(value1, value2)}"