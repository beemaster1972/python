def win(n: int, k: int):
    return 1 if n == 1 else 1+ (win(n-1,k)+k-1) % n


n, k = (int(input()) for _ in '12')
print(win(n,k))

# num = input()
# for idx in range(len(num) - 3, 0, -3):
#     num = num[:idx] + ',' + num[idx:]
# print(num)

# n =input()
# N = len(n)
# st, j = '', 0
# for i in range(-3,-N,-3):
#     st = ',' + n[i:N-j]+st
#     j += 3
# st = n[0:N-j] + st
# print(st)

# n = input()
# print(int(n[::-1]) if len(n) < 6 else int(n[0]+n[:0:-1]))


# horo_st ='Дракон Змея Лошадь Овца Обезьяна Петух Собака Свинья Крыса Бык Тигр Заяц'
# horo_d = {i:x for i,x in enumerate(horo_st.split())}
# year = int(input())
# print(horo_d.get((year-2000)%12))

# # put your python code here
# weight, height = (float(input()) for _ in range(2))
# imb = weight / height ** 2
# if 18.5 <= imb <= 25:
#     res = 'Оптимальная масса'
# elif 18.5 < imb:
#     res = 'Недостаточная масса'
# elif 25 > imb:
#     res = 'Избыточная масса'
#
# print(res, imb)