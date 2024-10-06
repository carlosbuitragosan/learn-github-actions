class Calculator:
    def __init__(self, value=0)
        self.value = value

    def add(self, x):
        self.value += x
        return self.value

    def subtract(self, x)
        self.value -= x
        return self.value

    def multiply(self, x):
        self.value *= x
        return self.value

    def divide(self, x):
        if x == 0:
            print("Error: Division by zero")
        else
            self.value /= x
        return self.value

    def reset(self)
        self.value = 0
        return self.value

calc = Calculator(10
print("Initial value:", calc.value)

calc.add(5
print("After adding 5:", calc.value)

calc.subtract(3
print("After subtracting 3:", calc.value)

calc.multiply(2
print("After multiplying by 2:", calc.value)

calc.divide(0
print("After attempting to divide by 0:", calc.value)

calc.reset(
print("After reset:", calc.value)
