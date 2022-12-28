n = int(input())
lst = [i for i in range(1,n+1) if n % i == 0]
print(*lst)
# n = int(input())
# b = [5000,2000,1000,200,100,50,10,5,2,1]
# m =[]
# d = n
# while d > 0:
#     for i,bn in enumerate(b):
#         k = d // bn
#         d %= bn
#         for j in range(k):
#             m.append(bn)
# print(*m)

# lst_in = ['django chto  eto takoe    poryadok ustanovki',
#           'model mtv   marshrutizaciya funkcii  predstavleniya',
#           'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
# for i,st in enumerate(lst_in):
#     s = st.replace(' ','-')
#     s1 = ''
#     while s != s1:
#         s1 = s
#         s = s.replace('--','-')
#     print(s)
#     lst_in[i] = s
# print(*lst_in, sep='\n')


# i, n = 0, list(map(int, input().split()))
# x = len(n) * 2
# while i < x:
#     n.insert(i+1,n[i])
#     i += 2
#     # if i == len(n) *2:
#     #     break
# print(*n)

# import re
# expr = input().replace(" ", "")
# numbers = list(map(int, re.split("\+|-", expr)))
# operand = re.findall('\+|-',expr)
# res = numbers[0]
#
# for i in range(1,len(numbers)):
#     if operand[i-1] == '+':
#         res += numbers[i]
#     else:
#         res -= numbers[i]
# # for j,c in enumerate(expr):
# #     if c in '+-':
# #         operand[j+1] = c
# print(res, eval(expr))


# phone = input()
# template = ["+","7","(",True,True,True,")",True,True,True,"-",True,True,"-",True,True]
# tmpl = [0,1,2,6,10,13]
# for i,c in enumerate(phone):
#     if len(phone) != len(template):
#         print('НЕТ')
#         break
#     if i in tmpl:
#         if c != template[i]:
#             print('НЕТ')
#             break
#     else:
#         if c.isdigit() != template[i]:
#             print('НЕТ')
#             break
# else:
#     print('ДА')



# s = input()
# ind = -1
# s.is
# for i in range(s.count('ра')):
#     ind = s.find('ра', ind+1)
#     print(ind, end=' ')
# print(ind if ind == -1 else '')
# n = [i for i in range(10,-1,-1)]
# print(*n)

# book, i = ["Муму","Евгений Онегин","Сияние","Мастер и Маргарита","Пиковая дама","Колобок"], 0
# while i < len(book):
#     if " " in book[i]:
#         book.pop(i)
#     else:
#         i += 1
# print(*book)


# cities = input().split()
# i = 0
# while i < len(cities):
#     if len(cities[i]) > 5:
#         print('ДА')
#         break
#     i += 1
# else:
#     print('НЕТ')


# n = int(input())
# a = 1
# while n > 0:
#     a *= 2
#     n -= (n % 3)
# print(a)


# s = input()
# while '--' in s:
#     s.replace('--','-')
# print(s)

# for sec in range(60):
#     print(sec + 1 if sec - 59 else 0)
# s = input()
# msg = "палиндром" if s.lower() == sorted(s.lower(),reverse=True) else "не палиндром"
# print(s[::-1].lower())
# m, n = map(int, input().split())
# m_all = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if n == m_all[m]:
#     print(str(m).rjust(2, '0') + '.' + str(m_all[m] - 1).rjust(2, '0') + ' ' + str(m + 1).rjust(2, '0') + '.01')
# elif n == 1:
#     print(str(m - 1).rjust(2, '0') + '.' + str(m_all[m - 1]).rjust(2, '0') + ' ' + str(n + 1).rjust(2, '0') + '.' + str(m).rjust(2, '0'))
# else:
#     print(str(m).rjust(2, '0') + '.' + str(n - 1).rjust(2, '0') + ' ' + str(m).rjust(2, '0') + '.' + str(n + 1).rjust(2, '0'))