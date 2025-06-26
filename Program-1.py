class Calculator:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def calculate(self, o):
        if o == "addition":
            return self.a + self.b
        if o == "subtraction":
            return self.a - self.b
        if o == "multiplication":
            return self.a * self.b
        if o == "division":
            return self.a / self.b if self.b else "Not divisible by 0"

try:
    a = float(input("Enter first value: "))
except ValueError:
    print("Invalid input. Enter a number.")
    exit()

try:
    b = float(input("Enter second value: "))
except ValueError:
    print("Invalid input. Enter a number.")
    exit()

o = input("Operation (addition, subtraction, multiplication, division): ")
if o not in ["addition", "subtraction", "multiplication", "division"]:
    print("Invalid operation. Please enter one of: addition, subtraction, multiplication, division.")
    exit()

result = Calculator(a, b).calculate(o)

print("Result:", int(result) if isinstance(result, float) and result.is_integer() else result)
