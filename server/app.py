#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    result = '\n'.join(str(i) for i in range(parameter))
    return result + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    result = 0
    num1 = int(num1)
    num2 = int(num2)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
        result = num1 % num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Zero Division Error'
    else:
        return 'Enter a valid input'
    
    return f'{result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
