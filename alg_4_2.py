#  Написать два алгоритма нахождения i-го по счёту простого числа.

import math

# без решета

def no_sieve_eratoshenes(i):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
            if flag:
                lst_prime.append(number)
            number += 1
        return lst_prime[-1]



# Через решето Эратосфена


def sieve_eratoshenes(i):
    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
            else:
                break


def prime_counting_function(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number/math.log(number)
        number += 1
        return number