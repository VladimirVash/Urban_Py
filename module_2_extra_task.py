def get_password(n):

    l = []

    for i in range(1, n):
        for j in range(1, n):
            if n % (i + j) == 0 and i != j:
                comb = ''.join(map(str, sorted([i, j])))
                if comb not in l:
                    l.append(comb)
    else:
        result = ''.join(l)
        return result

for i in range(3, 21):
    print(f'{i}: {get_password(i)}')