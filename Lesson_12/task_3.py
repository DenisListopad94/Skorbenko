class Life:
    def __init__(self, age):
        self.age = age


    def gobble(self, eat):
        pass


    def status(self):
        pass


class Fox(Life):
    def gobble(self, eat):
        if isinstance(eat, Rabbit):
            print('Лиса съела кролика')
        else:
            print('Лиса не может съесть эту пищу')


    def status(self):
        if self.age >= 7:
            print('Лиса умерла от старости')


class Rabbit(Life):
    def gobble(self, eat):
        if isinstance(eat, Plant):
            print('Кролик съел растение')
        else:
            print('Кролик не может съесть эту пищу')


    def status(self):
        if self.age >= 5:
            print('Кролик умер от старости')


class Plant(Life):
    def gobble(self, eat):
        print('Растение не может поглощать пищу')


    def status(self):
        if self.age >= 3:
            print('Растение завяло и умерло')


fox = Fox(7)
rabbit = Rabbit(2)
plant = Plant(1)

fox.gobble(rabbit)
fox.gobble(plant)

fox.status()
rabbit.status()
plant.status()
