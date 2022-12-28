s = input()
s_lst = s.split()

# здесь продолжайте программу
tp = tuple(tuple(s.split('=')) for s in s_lst)
print(tp)