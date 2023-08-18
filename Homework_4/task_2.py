# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопроцессорность.
# В решении нужно вывести время выполнения вычислений.

from multiprocessing import Pool
from random import randint
import time

start_time = time.time()


def sum_array(my_arr):
    res = 0
    for i in my_arr:
        res += i
    print(f'Result = {res:_}')
    return res


def main(sep_list):
    pool = Pool(processes=10)
    result = pool.map(sum_array, sep_list)
    return sum(result)


if __name__ == '__main__':
    my_array = [randint(1, 100) for _ in range(1_000_000)]
    split_array = [my_array[i:i + 100_000] for i in range(0, 1_000_000, 100_000)]
    results = main(split_array)

    print(f'\nSum of array elements = {results:_}')
    print('Verdict: Ok' if sum(my_array) == results else 'Verdict: Fail')
    print(f'Time taken: {time.time() - start_time:.10f} sec.')
