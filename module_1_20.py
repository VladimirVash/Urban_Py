# работа со словарем
my_dict = {'Петя':2003, 'Лена':2005, 'Вика':2003, 'Макс':2004, 'Влад':2004 }
print(my_dict)
print(my_dict['Лена'])
print(my_dict.get('Вова'))

my_dict.update({'Маша':2003, 'Вася':2005})
print(my_dict)
deleted = my_dict.pop('Петя')
print(deleted)
print(my_dict)

# работа со множествами
my_set = {'apple', 'orange', 'bread', 11, 10, 11, 'apple', 'orange'}
print(my_set)
# my_set.add('lemon')
my_set.add(('grapefruit', 'lemon'))
print(my_set)
my_set.discard('bread')
print(my_set)