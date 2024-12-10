def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
# print_params(a, b) NameError: name 'a' is not defined
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [3.7, 'строка', (1,2,3)]
values_dict = {'a':5, 'b':'string', 'c':False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [6, 8]

print_params(*values_list_2)
print_params(*values_list_2, 42)