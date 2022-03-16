from flask import Flask, request
import re

app = Flask(__name__)


@app.route("/index")
def index():
    return "Welcome to the Calculator App!!"


@app.route("/calculate")
def calculate():
    var_1 = request.args.get("var_1")
    var_2 = request.args.get("var_2")
    operator = request.args.get("operator")

    print(var_1, var_2, type(operator), "*****************")

    if (
        re.fullmatch("[0-9]*?[.][0-9]*|[0-9]*", var_1) != None
        and re.fullmatch("[0-9]*?[.][0-9]*|[0-9]*", var_2) != None
        and re.fullmatch(" |-|/|x", operator) != None
    ):
        try:
            var_1 = int(var_1) if "." not in var_1 else float(var_1)
            var_2 = int(var_2) if "." not in var_2 else float(var_2)
            operator = "+" if operator == " " else operator
            output = eval(f"{var_1}{operator}{var_2}")

            return {"result": output}, 200
        except ZeroDivisionError as err:
            return {"message": "Internal Server Error", "error": f"{err}"}, 500
    else:
        return {
            "message": "Invalid Parameters",
            "var_1": "only integer and floats",
            "var_2": "only integer and floats",
            "operator": "allowed operators : +,-,x,/",
        }, 403


if __name__ == "__main__":
    app.run(debug=True)
