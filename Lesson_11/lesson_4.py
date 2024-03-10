class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        self.coins += v


money_box = MoneyBox(10)
print(money_box.can_add(5))
money_box.add(5)
print(money_box.can_add(6))
