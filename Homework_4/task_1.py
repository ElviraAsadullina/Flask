# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность.
# В решении нужно вывести время выполнения вычислений.

import threading
import time
from random import randint

my_array = [randint(1, 100) for _ in range(1_000_000)]
result = 0
start_time = time.time()


def get_sum(go, stop, num):
    global result
    for i in range(go, stop):
        result += my_array[i]
    print(f'{num}. Result = {result:_}')


threads = []
for j in range(10):
    start = j * 100000
    end = start + 100000
    t = threading.Thread(target=get_sum, args=[start, end, j + 1])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'\nSum of array elements = {result:_}')
print('Verdict: Ok' if sum(my_array) == result else 'Verdict: Fail')
print(f'Time taken: {time.time() - start_time:.10f} sec.')
