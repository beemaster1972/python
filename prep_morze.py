from morze import morze_rus

lst = [[vol,key] for key,vol in morze_rus.items()]
print(lst)
rus_morze = dict(lst)
print('rus_morze =', rus_morze)
# st = input().strip()
# st_out = ''
# for i in range(len(st)):
#     st_out = st_out + morze_rus[st[i].lower()] if st[i] != ' ' else morze_rus['space']
# print(st_out)
# for c in st_out:
#     if c == '.':
#         pysine.sine(frequency=220, duration=0.1)
#         pysine.sine(frequency=30, duration=0.1)
#     else:
#         pysine.sine(frequency=220, duration=0.3)
#         pysine.sine(frequency=30, duration=0.1)