


# put your python code here
from functools import wraps


start = int(input())

def decor(start):


    def get_sum_decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + start


        return wrapper
    return get_sum_decor

@decor(start)
def get_sum(s):
    """Возвращает сумму списка целых чисел
    """
    return sum(list(map(int, s.split())))


n = input()
print(get_sum(n))