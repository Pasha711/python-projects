class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return ("Cannot divide by zero.")


calculator = Calculator()

result = calculator.add(7, 5)
print("7 + 5 =", result)

result = calculator.subtract(34, 21)
print("34 - 21 =", result)

result = calculator.multiply(54, 2)
print("54 * 2 =", result)

result = calculator.divide(144, 2)
print("144 / 2 =", result)

result = calculator.divide(45, 0)
print("45 / 0 =", result)
