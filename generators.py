import math
i = 3
def gen_prime():
    global i
    while True:

        for j in range(3, math.floor(pow(i, 1 / 2)) + 1, 2):
            if i % j == 0:
                fl = False
                break
        else:
            res = i
            i += 2
            yield res
        i += 2

print("2", end=' ')
for _ in range(19):
    print(next(gen_prime()), end=' ')

# def tribonacci(num: int):
#     first, second, third = 1, 1, 1
#     while True:
#         yield first
#         first, second, third = second, third, first + second + third
#
#
# n = int(input())
# tribo = tribonacci(n)
#
# print(*(next(tribo) for _ in range(n)))



# N = int(input())
# assert N > 5, "N должно быть больше 5"
#
# n1 = n2 = n3 = summ = 1
#
#
# def tribonachi(N):
#     """ Возвращает число трибоначи для N"""
#     global n1, n2, n3, summ
#
#     n1 = summ if N % 3 == 0 else n1
#     n2 = summ if N % 3 == 1 else n2
#     n3 = summ if N % 3 == 2 else n3
#     summ = 1 if N <= 3 else n1 + n2 + n3
#     return summ
#
#
# for i in range(1, N + 1):
#     print(tribonachi(i), end=' ')


# from numpy import arange
# a, b = list(map(int, input().split()))
# gen = ((lambda x: round(0.5 * pow(x, 2) - 2.0, 2))(x) for x in arange(a, b+1, 0.01))
# for i in range(20):
#     print(next(gen), end=' ')


# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# gen = (city for i in range(1000000)  for city in cities)
# for i in range(20):
#     print(next(gen),end=' ')


# from string import ascii_lowercase as lc
# comb = (lc[i]+lc[j] for i in range(len(lc)) for j in range(len(lc)))
# for i in range(50):
#     print(next(comb))