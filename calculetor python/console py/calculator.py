import re
import ast

def calculate_expression(expression):
    """
    Calculate the result of a mathematical expression.

    Args:
        expression (str): A string representing a mathematical expression.

    Returns:
        float or str: The result of the mathematical expression if valid, or an error message if the expression is invalid.
    """
    try:
        # Ensure the expression is wrapped in parentheses and evaluate it as a string
        result = ast.literal_eval("(" + expression + ")")
        return result
    except (SyntaxError, ValueError) as e:
        return str(e)

def main():
    print("Welcome to the Modern Web Calculator!")
    print("You can perform basic arithmetic operations (+, -, *, /) and use parentheses.")
    print("Type 'exit' to quit.")

    while True:
        expression = input("Enter a mathematical expression: ")
        
        if expression.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the input contains only allowed characters
        if re.match(r'^[0-9+*/().\- ]+$', expression):
            result = calculate_expression(expression)
            print("Result: " + str(result))
        else:
            print("Invalid input. Please enter a valid mathematical expression.")

if __name__ == "__main__":
    main()
