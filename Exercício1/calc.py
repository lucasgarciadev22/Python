import math


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def verify_nums(self):
        if self.num1 == 0:
            self.num1 = 5
        if self.num2 == 0:
            self.num2 = 5

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Can't divide by zero"

    def exp(self):
        return self.num1 ** self.num2

    def rem(self):
        return self.num1 % self.num2

    def sqrt_sum(self):
        return math.sqrt(self.num1 + self.num2)
