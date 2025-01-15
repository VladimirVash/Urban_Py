class Product:

    def __init__(self, product, weight, category):
        self.product = product
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.product}, {self.weight}, {self.category}'

class Shop:

    __file_name = 'products.txt'

    def get_products(self):                 # Я пытался сделать через print и через return
        file = open(self.__file_name, 'r')  # Если делать через print, то выдает None, что является неверным подходом
        res = file.read()                   # Если делать через return, то файл не закроется, что логично
        file.close()                        # Поэтому я решил записать результат чтения в переменную res
        return res                          # И потом просто закрыть и через return вернуть результат чтения файла (без костылей не обошлось)

    def add(self, *products):
        for meal in products:
            file = open(self.__file_name, 'r')
            if f'{meal.product}, {meal.weight}, {meal.category}'  in file.read() :
                print(f'Продукт {meal.product} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{meal.product}, {meal.weight}, {meal.category}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())



