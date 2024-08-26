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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
