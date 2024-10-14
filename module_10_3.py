from threading import Thread, Lock
import random
from time import sleep
import threading


class Bank:

    def __init__(self):
        super().__init__()
        self.lock = Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            n = random.randint(50, 500)
            self.balance += n
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += n
            print(f' Пополнение: {n}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            a = random.randint(50, 500)
            print(f' Запрос на {a}')
            if a <= self.balance:
                self.balance -= a
                print(f' Снятие: {a}. Баланс: {self.balance}')
            else:
                print(f' Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()
print(f' Итоговый баланс: {bk.balance}')
