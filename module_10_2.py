from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        number_of_enemies = 100
        calc = 0
        while number_of_enemies > 0:
            number_of_enemies -= self.power
            calc += 1
            sleep(1)
            print(f'{self.name} сражается {calc} дней, осталось {number_of_enemies} врагов\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
