"""
Calculator Module

This module provides a basic web calculator functionality using Flask.
"""


import ast
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """
    Calculate Function
    
    This function evaluates the mathematical expression provided by the user.

    Parameters:
    - request.form['expression']: str, the mathematical expression to be evaluated
    
    Returns:
    - dict: A dictionary containing the result of the evaluation or an error message.
    """
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Calculate Function
    
    This function evaluates the mathematical expression provided by the user.

    Parameters:
    - request.form['expression']: str, the mathematical expression to be evaluated
    
    Returns:
    - dict: A dictionary containing the result of the evaluation or an error message.
    """
    try:
        expression = request.form['expression']
        result = str(ast.literal_eval(expression))
        return jsonify({'result': result})
    except (SyntaxError, ValueError) as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
