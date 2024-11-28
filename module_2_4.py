def get_matrix(n, m, val):

    matrix = []
    col = []

    for rows in range(n):
        for cols in range(m):
            col.append(val)
        else:
            matrix.append(col)
            col = []
    else:
        return matrix

n = int(input('Введите количество строк: '))
m = int(input('Введите количество колонок: '))
val = int(input('Введите значение, которым заполнить матрицу: '))

print(*get_matrix(n,m,val), sep='\n')
