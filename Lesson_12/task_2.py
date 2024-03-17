class Carrier:
    def __init__(self, name):
        self.name = name


    def calc_time(self, distance):
        raise NotImplementedError

    def calc_price(self, distance):
        raise NotImplementedError


class Plane(Carrier):
    def __init__(self, name, speed, price_per_km):
        super().__init__(name)
        self.speed = speed
        self.price_per_km = price_per_km


    def calc_time(self, distance):
        return distance // self.speed

    def calc_price(self, distance):
        return distance * self.price_per_km

class Train(Carrier):
    def __init__(self, name, speed, price_per_km):
        super().__init__(name)
        self.speed = speed
        self.price_per_km = price_per_km


    def calc_time(self, distance):
        return distance // self.speed

    def calc_price(self, distance):
        return distance * self.price_per_km


class Car(Carrier):
    def __init__(self, name, speed, price_per_km):
        super().__init__(name)
        self.speed = speed
        self.price_per_km = price_per_km


    def calc_time(self, distance):
        return distance // self.speed

    def calc_price(self, distance):
        return distance * self.price_per_km


plane = Plane("Самолет", 800, 10)
train = Train("Поезд", 100, 5)
car = Car("Машина", 120, 7)

# расстояние между городами
distance = 1000

print("Время и стоимость транспортировки:")
print("Самолет:")
print("Время: ", plane.calc_time(distance), "часы")
print("Цена: $", plane.calc_price(distance))
print("Поезд:")
print("Время: ", train.calc_time(distance), "часы")
print("Цена: $", train.calc_price(distance))
print("Машина:")
print("Время: ", car.calc_time(distance), "часы")
print("Цена: $", car.calc_price(distance))