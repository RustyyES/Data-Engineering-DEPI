class Calculator:
    def __init__(self, first: int | float, second: int | float):
        self.first = first
        self.second = second

    def addition(self):
        return self.first + self.second

    def subtraction(self):
        return self.first - self.second

    def multiply(self):
        return self.first * self.second

    def divide(self):
        if self.second == 0:
            raise ZeroDivisionError("You can't divide by zero")
        return self.first / self.second


if __name__ == "__main__":
    while True:
        try:
            x, y = map(
                float,
                input(
                    "Enter first number and second number with a space in between\n"
                ).split(),
            )
            break
        except ValueError:
            print("Invalid type, please enter a number.\n")
    while True:
        try:
            p = int(input("Enter operation number 1-add 2-sub 3-mul 4-div\n"))
            if 1 <= p <= 4:
                break
            else:
                print("Error: Please enter a number between 1 and 4\n")
        except ValueError:
            print("Invalid input. please enter a number. \n")
    calc = Calculator(x, y)
    operations = {
        1: calc.addition,
        2: calc.subtraction,
        3: calc.multiply,
        4: calc.divide,
    }
    try:
        result = operations[p]()
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
