# Lambda-функция:
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

result =  list(map(lambda l1, l2: l1 == l2, first, second))
print(result)


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file: # поставил 'w', чтобы при моей проверке не засоряло файл лишний раз
            for el in data_set:
                file.write(str(el)+'\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())