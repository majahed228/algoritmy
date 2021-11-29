# Определить, какое число в массиве встречается чаще всего.

import random

a = [random.randint(0, 50) for n in range(100)]
print(a)
max_index = 0

for i in a:
    if a.count(max_index) < a.count(i):
        max_index = a.index(i)

print(f'Чаще всего встречается число {max_index}: {a.count(max_index)} раз')


