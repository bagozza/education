from threading import Thread
from random import randint
from time import sleep
from queue import Queue


class Guest(Thread):
    def __init__(self, number: int):
        super().__init__()
        self.number = number

    def run(self):
        sec = randint(3, 10)
        sleep(sec)


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest: Guest | None = None


class Cafe:
    def __init__(self, *tables: Table):
        self.tables = list(tables)
        self.queue: Queue[Guest] = Queue()

    def get_empty_tables(self):
        for table in self.tables:
            if table.guest is None:
                yield table

    def get_not_empty_tables(self):
        for table in self.tables:
            if table.guest is not None:
                yield table

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            is_seat = False
            for table in self.get_empty_tables():
                table.guest = guest
                table.guest.start()
                print(f'{guest.name}, сел(-а) за стол номер {table.number}')
                is_seat = True
                break
            if not is_seat:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while (not self.queue.empty() or
               any(self.get_empty_tables())):
            for table in self.get_not_empty_tables():
                if not table.guest.is_alive():
                    print(f'{table.guest.name} покушал и ушел')
                    table.guest = None
                    print(f'Стол номер {table.number} освободился')
            if not self.queue.empty():
                for table in self.get_empty_tables():
                    guest = self.queue.get()
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
