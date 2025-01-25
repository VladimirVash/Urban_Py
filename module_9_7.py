def is_prime(func):
    def origin(*args):
        res = func(*args) # распаковываем наши три элемента
        for i in range(2, int(res/2) + 1):
            if res % i == 0:
                print('Сложное')
                return res
        else:
            print('Простое')
            return res
    return origin


@is_prime
def sum_three(first, second, third):
    return sum([first, second, third])


result = sum_three(2, 3, 6)
print(result)