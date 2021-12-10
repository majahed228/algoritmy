# Посчитать четные и нечетные цифры введенного натурального числа.

number = input('Введите число:')
chet = 0
nechet = 0
for f in number:
    i = int(f)
    if i % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(f'Четных - {chet}, нечетных - {nechet}')