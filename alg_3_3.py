# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(0, 99) for n in range(10)]
print(f'Массив до изменний : {a}')

max = a[0]
min = a[0]

for i in a:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = a.index(min)
max_index = a.index(max)
a[min_index], a[max_index] = a[max_index], a[min_index]
print(f'Массив после изменения элементов: {a} ')

