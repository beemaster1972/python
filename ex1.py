# import math

m , n = map(int, input().split())
dom = [31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]
mp , dp , mn , dn = 1 , 1 , 1 , 1
if n == 1:
    mp = m - 1
    dp = dom[mp-1]
    mn = m
    dn = n + 1
elif 1 < n < dom[m-1]:
    mp , mn = m , m
    dp = n - 1
    dn = n + 1
elif n == dom[m-1]:
    mp = m
    mn = m + 1
    dp = n -1
    dn = 1
print(f'{mp:02}.{dp:02} {mn:02}.{dn:02}')

# lst = list(x for x in input())
# print(lst)
# lst = lst[2:]
# lst.insert(0,'8')
# lst.remove('-')
# lst.remove('-')
# print("".join(lst))

# title, author, pages, price = input(), input(), int(input()), float(input())
# book = [title, author, pages, price]
# book.remove(book[2])
# book[1] = 'Пушкин'
# book[2] *=2
# print(book)
# marks = list(map(int, input().split()))
# print(sum(marks)/len(marks))

# lst = list(map(int,input().split()))
# lst.sort()
# print(*lst)


# s1 = input()
# s2 = input()
# print(' '.join([s1,s2]))
# print([21, 13].sort())
# n, m, vm = map(int, input('Введите кол-во детей, вожатых и вместимость одного автобуса через пробел').split())
# # C = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
# # print(C)
#
# a = (n + m) // vm if (n + m) % vm == 0 else (n + m) // vm + 1
# print(a)
# x, skidka = map(int, input('Сколько стоит одна ручка и процент скидки? ').split())
# x *= 1-(skidka/100)
# kol = math.floor(500 / x)
# print(kol)
# a, b = map(float,input().split())
# print(a + b)
# price = float(input())
# print(price%1 > 0.50)
# a, b, c = map(int, input().split())
# print(a < b+c and b < a+c and c < a+b)
# a = float(input())
# print((0 <= a <= 2) or (10 <= a <= 20))