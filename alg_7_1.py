# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
import random


def bubble_sort(array):
    li = array
    n = 1
    while n < len(li):
        for i in range(len(li) - n):
            if li[i] > li[i + 1]:
                li[i], li[i+1] = li[i+1], li[i]
        n += 1
    return array


numbers = [random.randint(-100, 100) for _ in range(10)]
print(f'Массив до сортировки: {numbers}')
print(f'Массив после сортировки пузырьком: {bubble_sort(numbers)}')