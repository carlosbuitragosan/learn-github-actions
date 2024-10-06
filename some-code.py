class Calculator:
    def __init__(self, value=0):  # Added colon
        self.value = value

    def add(self, x):
        self.value += x
        return self.value

    def subtract(self, x):  # Added colon
        self.value -= x
        return self.value

    def multiply(self, x):
        self.value *= x
        return self.value

    def divide(self, x):
        if x == 0:
            print("Error: Division by zero")
        else:
            self.value /= x  # Fixed indentation of else statement
        return self.value

    def reset(self):  # Added colon
        self.value = 0
        return self.value

calc = Calculator(10)  # Added closing parenthesis
print("Initial value:", calc.value)

calc.add(5)  # Added closing parenthesis
print("After adding 5:", calc.value)

calc.subtract(3)  # Added closing parenthesis
print("After subtracting 3:", calc.value)

calc.multiply(2)  # Added closing parenthesis
print("After multiplying by 2:", calc.value)

calc.divide(0)  # Added closing parenthesis
print("After attempting to divide by 0:", calc.value)

calc.reset()  # Added closing parenthesis
print("After reset:", calc.value)
