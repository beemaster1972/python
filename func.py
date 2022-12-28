t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


# здесь продолжайте программу
def decor(chars=" !?"):

    def replace_dash(func):


        def wrapper(*args, **kwargs):
            s = func(*args, **kwargs)
            s = ''.join(['-' if s[i] in chars else s[i] for i in range(len(s))])
            for i in range(s.count('--')+1):
                s = s.replace('--', '-')
            return s

        return wrapper

    return replace_dash


@decor(chars="?!:;,. ")
def convert_cyr_lat(s):
    s = s.lower()
    return ''.join([t[s[i]] if s[i] in t else s[i] for i in range(len(s))])


print(convert_cyr_lat(input()))



# # put your python code here
# def dict_from_list(func):
#     def wrapper(*args, **kwargs):
#         return dict(func(*args, **kwargs))
#
#     return wrapper
#
#
# @dict_from_list
# def get_lists(st1, st2):
#     return list([st1.split()[i], st2.split()[i]] for i in range(len(st1.split())))
#
#
# d = get_lists(input(), input())
# print(*sorted(d.items()))



# # put your python code here
# def sort_lst(func):
#     def wrapper(*args, **kwargs):
#         return sorted(func(*args), **kwargs)
#
#     return wrapper
#
#
# @sort_lst
# def get_list(st, *args, **kwargs):
#     return list(map(int, st.split()))
#
#
# lst = get_list(input(), reverse = True)
# print(*lst)



# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return res
#
# # здесь продолжайте программу
# lst = list(map(int, input().split()))
# print(*filter_lst(lst))
# print(*filter_lst(lst,lambda x: x <0))
# print(*filter_lst(lst,lambda x: x >=0))
# print(*filter_lst(lst,lambda x: x[3:5]))


# lst = list(map(int, input().split()))
#
# def merge_sorted(l,r):
#     res=[0 for i in range(len(l) + len(r))]
#     i = k = n = 0
#     while i < len(l) and k < len(r):
#         res[n] = l[i] if l[i] <= r[k] else r[k]
#         n += 1
#         if l[i] <= r[k]:
#             i += 1
#         else:
#             k += 1
#     while len(res) > n:
#         res.pop()
#     res += l[i:] + r[k:]
#     return res
#
# def sort_merge(l:list):
#     if len(l) == 1:
#         return l
#     M = len(l) // 2
#     L = sort_merge(l[0:M])
#     R = sort_merge(l[M:])
#     return merge_sorted(L,R)
#
# print(*sort_merge(lst))

# N = int(input())
#
# def get_path(n):
#     if n == 2:
#         return 2
#     elif n < 2:
#         return 1
#     return get_path(n-1) + get_path(n-2)
#
# print(get_path(N))




# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#
# # здесь продолжайте программу
# def get_line_list(d,a=[]):
#     for x in d:
#         if type(x) != list:
#             a.append(x)
#         else:
#             get_line_list(x,a)
#     return a
#
# print(d, get_line_list(d))


# import math
# # ввод числа n
# n = int(input())
#
# # здесь задается функция fact_rec  (переменную n не менять!)
# def fact_rec(n):
#     if n == 0:
#         return 1
#     return fact_rec(n-1) * n
#
# print(fact_rec(n), math.factorial(n))

# ввод числа N
# N = int(input())
#
#
# # здесь задается функция fib_rec (переменную N не менять!)
# def fib_rec(N, f=[1,1]):
#     if N == 1:
#         f = [1]
#         return f
#     elif N == 2:
#         f = [1, 1]
#         return f
#     fib_rec(N - 1, f)
#     f.append(f[N - 3] + f[N-2])
#     return f
#
#
# print(*fib_rec(N))

# lst_in = ["Города=about-cities",
#           "Машины=read-of-cars",
#           "Самолеты=airplanes"]
#
#
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# # здесь продолжайте программу (используйте список lst_in и menu)
# d = dict([x.split('=') for x in lst_in])
# menu = {*menu.items(), *d.items()}
# print(menu)


# mtrx = [[1, 0, 0, 0, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0]]

# def is_isolate(matrix):
#     return sum(matrix[0]) == 0 and sum(matrix[1]) == 1 and sum(matrix[2]) == 0
#
#
# def verify(matrix):
#     N = len(matrix[0])
#     for row in matrix:
#         row.insert(0,0)
#         row.append(0)
#     zero = [0 for i in range(N+2)]
#     matrix.insert(0,zero)
#     matrix.append(zero)
#     # for row in matrix:
#     #     print(*row)
#     for i in range(1,N):
#         for j in range(1,N):
#             if matrix[i][j] == 1:
#                 if not is_isolate([[matrix[y][x] for x in range(j-1,j+2)] for y in range(i-1,i+2)]):
#                     return False
#     return True

# print(verify(mtrx))

# def get_data_fig(*args,**kwargs):
#     cort = sum(args),
#     if 'type' in kwargs:
#         cort += kwargs['type'],
#     if 'color' in kwargs:
#         cort += kwargs['color'],
#     if 'closed' in kwargs:
#         cort += kwargs['closed'],
#     if 'width' in kwargs:
#         cort += kwargs['width'],
#     return cort


# print(get_data_fig(1,2,3,4,5,6,7,8,9,type=False,color=120,closed=True,width=11))


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# def cyr_2_lat(s, sep = '-'):
#     lat = [t[i] if i in t else i for i in s.lower()]
#     return ''.join(lat).replace(' ',sep)
#
#
# print(cyr_2_lat('Лучший курс по Python!'))
# print(cyr_2_lat('Лучший курс по Python!','+'))

# def get_str(s):
#     return s, len(s)
#
#
# cities = input()
# d = {get_str(x)[0]:get_str(x)[1] for x in cities.split()}
# a = sorted(d, key=lambda x: d[x])
# print(*a)


# print(ord('0'),ord('9'))
# valid_chars = {chr(x) for x in range(97,123)}
# numbrs = {chr(x) for x in range(48,58)}
# valid_chars ^= numbrs
# valid_chars.add('_')
# valid_chars.add('@')
# valid_chars.add('.')
# #print(*sorted(valid_chars))
# def check_email(addr):
#     if type(addr) != str:
#         return False
#     if addr.find('@') <0 and addr.find('.') < 0:
#         return False
#     if set(addr) - valid_chars != {}:
#         return False
#     return True
#
# email_addr = input()
# if check_email(email_addr):
#     print('ДА')
# else:
#     print('НЕТ')
# print(*sorted(valid_chars))
# def print_weight(weight):
#     print(f'Предмет имеет вес: {weight:.2f} кг.')
#
# w = float(input())
# print_weight(w)
