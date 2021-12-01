# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def sum_numbers(number):
    sum = 0
    for f in number:
        sum += int(f)
    return sum


a, b = [i for i in input('Введите два числа:').split()]

max_number = 0
max_sum = 0
for i in a, b:
    if sum_numbers(i) > max_sum:
        max_number = i
        max_sum = sum_numbers(i)

print(f'У {max_number} : {max_sum}')