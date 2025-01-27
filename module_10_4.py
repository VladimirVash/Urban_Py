from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:

    def __init__(self, num, guest = None):
        self.number = num
        self.guest = guest

    def __str__(self):
        return f'Столик №{self.number}'



class Guest(Thread):

    def __init__(self, guest):
        super().__init__()
        self.guest = guest

    def __str__(self):
        return self.guest

    def run(self):
        sleep(randint(3, 10))



class Cafe:

    def __init__(self, *tables_):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for g in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = g
                    g.start()
                    print(f'{g} сел(-а) за стол номер {table}')
                    break
            else:
                self.queue.put(g)
                print(f'{g} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(t.guest is not None for t in self.tables):
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f'{t.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {t} свободен')
                    t.guest = None

            for t in self.tables:
                if not self.queue.empty() and t.guest is None:
                    t.guest = self.queue.get()
                    print(f'{t.guest} вышел(-ла) из очереди и сел(-а) за стол номер {t}')
                    t.guest.start()




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
cafe = Cafe(tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
