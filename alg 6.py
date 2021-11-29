#  Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

abc_nubmer = int(input('Введите номер буквы:'))

my_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(my_list)
if abc_nubmer <= len(my_list):
    print(f'Буква под номером {abc_nubmer}: {my_list[abc_nubmer - 1]}')
else:
    print(f'введите число не превышающее кол-во букв в алфавите ({len(my_list)})')

