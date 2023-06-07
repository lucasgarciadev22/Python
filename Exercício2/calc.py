class Calculator:
    def __init__(self, num1, num2, num3, vector_x):
        self.a = num1
        self.b = num2
        self.c = num3
        self.x = vector_x

    def linear_eq_calc(self):
        return [self.a * xi + self.b * xi - self.c for xi in self.x]
