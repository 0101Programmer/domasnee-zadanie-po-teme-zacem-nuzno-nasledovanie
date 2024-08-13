class Animal:

    def __init__(self, name, fed=False, alive=True):
        self.name = name
        self.fed = fed
        self.alive = alive

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Mammal('Панда По')
a2 = Predator('Лев Алекс')
p1 = Flower('Ядовитый одуванчик')
p2 = Fruit('Арбуз')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
