class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        house = super().__new__(cls)
        cls.houses_history.append(args[0])
        return house

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        self.houses_history.remove(self.name)
        print(f"{self.name} снесен, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
