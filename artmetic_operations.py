# This class does arithmetic operations
class ArthimeticClass:
    def add(x, y):
        # adding two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        return x + y
    def subtract(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        # subtracting two numbers
        return x - y
    def multiply(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        # multiplying two numbers
        return x * y
    def divide(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        
        elif y == 0:
            raise TypeError("the divisor should be different from zero")
        # dividing two numbers
        return x / y
