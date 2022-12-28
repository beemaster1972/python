lst_in = ['Главная home',
'Python learn-python',
'Java learn-java',
'PHP learn-php]']
menu = ()
for s in lst_in:
    menu += (tuple(s.split()),)
print(menu)

# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# N = int(input())
# t1 = ()
# for i in range(N):
#     t1 += tuple(t[i][:N+1])
# print(t1)
#for i in range(N):
    #print(*t2[i])

# t = tuple(input().split())
# for i in range(len(t)):
#     if t[i].lower().find('ва') >= 0:
#         print(t[i].lower(),end =' ')