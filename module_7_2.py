def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')

    res = {}

    for i, s in enumerate(strings):
        tell = file.tell()
        file.write(s+'\n')
        res[(i+1, tell)] = s
    else:
        file.close()
        return res

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
