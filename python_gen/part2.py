import math
import timeit
RO = 'ОРРОРОРООРРРОООООООРРРОРОРРРРРРРООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРОРОРООРРРОООООООРРРОРОРРРРРРРООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'
def a(RO):
    maxR = 0
    if 'Р' in RO:
        lst = tuple(RO)
        idx = lst.index('Р')
        while idx < len(lst):
            end = lst.index('О', idx+1) if 'О' in lst[idx:] else len(lst)
            maxR = end - idx if (end - idx) > maxR else maxR
            idx = lst.index('Р',end + 1) if 'Р' in lst[end+1:] else len(lst)

    print('моя функция ',maxR)


def b(RO):
    print('функция со сплитом ',len(max(RO.split('О'))))


print(timeit.timeit('a(RO)',number=1,globals=globals()))
print(timeit.timeit('b(RO)',number=1,globals=globals()))


# put your python code here
# lots = ["ножницы", "бумага", "камень", "ящерица", "Спок"]
# players = ['ничья', 'Тимур', 'Руслан']
# # idx = (lots.index(input())-lots.index(input())) % 5
# for T in lots:
#     for R in lots:
#         idx = (lots.index(T)-lots.index(R))%5
#         print(T, R , players[idx and idx % 2 + 1])

# print(players[table[lots[draw[1]]][lots[draw[0]]]])

# n = int(input())
# lst = [int(input()) for x in range(n)]
# prod = int(input())
# for i in range(len(lst) - 1):
#     for j in range(i + 1, len(lst)):
#         if lst[i] * lst[j] == prod:
#             print('ДА')
#             break
#
# else:
#     print('НЕТ')


# n = list(map(int, input().split()))
#
# for i in range(0,len(n)-1,2):
#     n[i], n[i+1] = n[i+1],n[i]
#
# print(*n)



# pcount = {'Первая четверть': 0, 'Вторая четверть': 0, 'Третья четверть': 0, 'Четвертая четверть': 0}
#
# n = int(input())
# coords = [list(map(int, input().split())) for i in range(n)]
# for row in coords:
#     if row[0] > 0 and row[1] > 0:
#         pcount['Первая четверть'] += 1
#     if row[0] < 0 and row[1] > 0:
#         pcount['Вторая четверть'] += 1
#     if row[0] <0 and row[1] < 0:
#         pcount['Третья четверть'] += 1
#     if row[0] > 0 and row[1] < 0:
#         pcount['Четвертая четверть'] += 1
# for k, v in pcount.items():
#     print(f'{k}: {v}')
