import multiprocessing
from multiprocessing import Pool
from time import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding= 'utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                all_data.append(line)



filenames = [f'file {number}.txt' for number in range(1, 5)]


if __name__ == '__main__':
    # Линейный вызов
    start = time()
    for file in filenames:
        read_info(file)
    final = time()
    print('Линейный вызов:',final - start)

    # Многопроцессный
    start = time()
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(read_info, filenames)
    final = time()
    print('Многопроцессный:',final - start)