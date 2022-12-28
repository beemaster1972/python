things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

pohod = {v:k for k,v in things.items()}

weight, back_pack = 0, []

N = int(input()) * 1000
while weight < N and len(things)>0:
    max_w = max(things.values())
    if weight + max_w <= N:
        back_pack.append(pohod[max_w])
        del things[pohod[max_w]]
        weight += max_w
    else:
        del things[pohod[max_w]]
print(weight)
print(*back_pack)

#3,Сергей 5,Николай 4,Елена 7,Владимир 5,Юлия 4,Светлана
# lst_in = input().split()
# d = {}
# for c in lst_in:
#     key, vol = c.split(',')
#     if key in d:
#         d[key].append(vol)
#     else:
#         d[key] = [vol]
# for key, vol in d.items():
#     print(f'{key}: ', ', '.join(vol),sep='')

# d = {}
# n = int(input())
# while  n != 0:
#     if n in d:
#         print(f'значение из кэша: {d[n]}')
#     else:
#         d[n] = round(n ** (1/2),2)
#         print(d[n])
#     n = int(input())

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# lst = [x.split() for x in lst_in]
# d = {}
# for i in lst:
#     if i[1] in d:
#         d[i[1]].append(i[0])
#     else:
#         d[i[1]] = [i[0]]
# print(*sorted(d.items()))

# lst_in = [[x[:2], [x]] for x in input().split()]
# lnght = len(lst_in)
# for i, row in enumerate(lst_in):
#     j = i + 1
#     while j < lnght:
#         if row[0] == lst_in[j][0]:
#             row[1].append(lst_in[j][1][0])
#             lst_in.remove(lst_in[j])
#             lnght -=1
#         j += 1
# d = dict(lst_in)
# print(*sorted(d.items()))

# d = dict(x.split('=') for x in input().split())
# keys = ['False','3']
# for k in keys:
#     if k in d:
#         del d[k]
# print(*sorted(d.items()))

# lst_in = ["5=отлично",
#           "4=хорошо",
#           "3=удовлетворительно"]
# lst = [x.split('=') for x in lst_in]
# d ={int(lst[i][0]):lst[i][1] for i in range(len(lst_in))}
# print(d)