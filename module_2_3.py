numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

not_primes = []
primes = []

for num in numbers:
    for j in range(2, num):
        if num % j == 0:
            not_primes.append(num)
            break
    else:
        primes.append(num)

print(primes)
print(not_primes)