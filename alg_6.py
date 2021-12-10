# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти

import sys

# Python 3.9.1,  windows x64

a, b, c = [int(x) for x in input('Введите длины сторон:').split()]

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')

else:
    print('Такого треугольника не существует!')


sum_size = 0
sum_size += sys.getsizeof(a)
sum_size += sys.getsizeof(b)
sum_size += sys.getsizeof(c)


print(f' Переменные занимают: {sum_size} '
      f' a:{sys.getsizeof(a)},'
      f' b:{sys.getsizeof(b)},'
      f' c:{sys.getsizeof(c)}')