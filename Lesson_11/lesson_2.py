class DecimalCounter:
    def __init__(self, min_value=0, max_value=10, initial_value=0):
        self.min = min_value
        self.max = max_value
        if initial_value < min_value or initial_value > max_value:
            raise ValueError("Начальное значение не находится в пределах указанного диапазона")
        self.value = initial_value

    def increase(self):
        if self.value < self.max:
            self.value += 1
        else:
            print("Не может превышать максимального значения")

    def decrease(self):
        if self.value > self.min:
            self.value -= 1
        else:
            print("Не может уменьшиться ниже минимального значения")

    @property
    def current_value(self):
        return self.value


counter = DecimalCounter(min_value=0, max_value=100, initial_value=50)

print(counter.current_value)

counter.increase()
print(counter.current_value)

counter.decrease()
print(counter.current_value)
counter.increase()
counter.increase()
print(counter.current_value)
