def get_sum(it):
    summ = sum(filter(lambda x: type(x) == int, it))
    for x in it:
        if type(x) in (list, tuple, set):
            summ += get_sum(x)
    return summ

print(get_sum([1,2,[3,4,5,'6'],(7,'8'),{9,10,11,'ff'}]))


# def get_similar(a,b):
#     if type(a) in (int,float) and type(b) in (int,float):
#         return True
#     elif type(a) == str and type(b) == str:
#         return True
#     else: return False
#
#
# def get_add(a,b):
#     return a + b if get_similar(a,b) else None
#
# print(get_add('15.3','10'))