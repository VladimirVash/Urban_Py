immutable_var = (1,2,3,4, False, 'Just string', [5,6,7])
print(immutable_var, '\n')

# immutable_var[4] = True - Получим ошибку, т.к. tuple неизменяемый объект
# но мы можем поменять значения внутри списка [5,6,7], потому что
# список является изменяемым объектом

# Например:
mutable_list = [1,2,3,4, False, 'Just string']
print(mutable_list,'\n')

mutable_list[5] = 'This string has been changed'
print(mutable_list)