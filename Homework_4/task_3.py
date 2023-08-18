# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать асинхронность.
# В решении нужно вывести время выполнения вычислений.

import asyncio
import random
import time

my_array = [random.randint(1, 100) for _ in range(1_000_000)]
start_time = time.time()


async def sum_array(start, end, num):
    res = sum(my_array[start:end])
    print(f'{num}. Result: {res:_}')
    return res


async def main():
    tasks = []
    for i in range(10):
        start = i * 100000
        end = start + 100000
        task = asyncio.create_task(sum_array(start, end, i + 1))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    print(f'\nSum of array elements = {sum(results):_}')
    print('Verdict: Ok' if sum(my_array) == sum(results) else 'Verdict: Fail')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

print(f'Time taken: {time.time() - start_time:.10f} sec.')
