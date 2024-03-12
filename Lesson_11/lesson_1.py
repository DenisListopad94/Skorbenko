class TwoNumber:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def display_var(self):
        print("Переменная 1:", self.num1)
        print("Переменная 2:", self.num2)

    def change_var(self, new_num1, new_num2):
        self.num1 = new_num1
        self.num2 = new_num2

    def sum_of_var(self):
        return self.num1 + self.num2

    def max_of_var(self):
        return max(self.num1, self.num2)


var = TwoNumber(5, 10)
var.display_var()

var.change_var(3, 7)
var.display_var()

print("Сумма чисел равна:", var.sum_of_var())
print("Максимальное число:", var.max_of_var())
