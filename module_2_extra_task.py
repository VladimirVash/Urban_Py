def get_password(n):

    l = [] # нужен для сбора уникальных значений, которые мы будем джойнить

    for first in range(1, n):
        for second in range(1, n):
            if n % (first + second) == 0 and first != second: # делаем проверку на подходящие комбинации
                comb = ''.join(map(str, sorted([first, second]))) # мэпим, чтобы получить комбинацию в виде строки из двух чисел
                if comb not in l: # проверяем на уникальность
                    l.append(comb) # добавляем уникальную комбинацию
    else:
        result = ''.join(l) # превращаем список из уникальных комбинаций в единую строку-пароль
        return result

for i in range(3, 21):
    print(f'{i} - {get_password(i)}') # делаем вывод для всех паролей по условию задачи

# если нужно именно конкретный пароль по цифре:
# n = int(input('Введите число для получения пароля: ')) 
# print(get_password(n))
