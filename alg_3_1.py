# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

result = {}
for f in range(2, 10):
    result[f] = []
    for n in range(2, 100):
        if n % f == 0:
            result[f].append(n)
    print(f'Числу {f} кратны {len(result[f])}. Кратные числа: {result[f]}')