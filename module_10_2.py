import threading
from time import sleep

class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.days = None
        self.name = name
        self.power = power

    def timer(self):
        enemies = 100
        days = 0
        while enemies != 0:
            enemies -= self.power
            days += 1

            if enemies < 0:
                enemies = 0

            print(f'{self.name} сражается {days} день(дня), осталось {enemies} воинов')
            sleep(1)
        else:
            return days

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = self.timer()
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
sleep(0.2) # чтобы при выводе в терминале друг к другу ничего не липло
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')