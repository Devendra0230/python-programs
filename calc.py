import sys


class HelpException(Exception):
    pass
    
def calculator(num1, op, num2):
    try:
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            return "Invalid operator"

        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    
    except:
        return "An error while performing the calculation"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python calc.py num1 op num2")
    else:
        num1 = float(sys.argv[1])
        op = sys.argv[2]
        num2 = float(sys.argv[3])

        result = calculator(num1, op, num2)
        print("Result:", result)
