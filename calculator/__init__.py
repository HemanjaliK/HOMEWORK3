from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a, b):
        # Directly return the result of the addition
        return add(a, b)

    @staticmethod
    def subtract(a, b):
        # Directly return the result of the subtraction
        return subtract(a, b)

    @staticmethod
    def multiply(a, b):
        # Directly return the result of the multiplication
        return multiply(a, b)

    @staticmethod
    def divide(a, b):
        # Directly return the result of the division
        return divide(a, b)
