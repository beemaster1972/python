
def nod(a, b):
    """
    Вычисление НОД по алшоритму Эвклида
    :param a: натуральное число
    :param b: натуральное число
    :return: НОД
    """
    if a < b:
        a,b = b,a
    while b !=0:
        a , b = b , a%b
    return a if a !=0 else b


x , y = 35 , 300000000003
print(f'НОД({x};{y}) = {nod(x,y)}')