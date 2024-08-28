class House:
    def __init__(self, name, floor):
        self.name = name
        self.numbers_of_floors = floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.numbers_of_floors:
            print('такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.numbers_of_floors} "


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(len(h1))
print(len(h2))
