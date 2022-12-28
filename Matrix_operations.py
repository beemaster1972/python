def addition_matrix(A : list, B : list, N : int, M : int) -> list:
    if len(A) != len(B) and len(A[0]) != len(B[0]):
        return None
    C = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            C[i][j] = A[i][j] + B[i][j]
    return C

# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# if len(a[0]) != m:
#     raise ValueError(' Ошибка в размерности матрицы A')
# input()
# b = [list(map(int, input().split())) for _ in range(n)]
# if len(b[0]) != m:
#     raise ValueError(' Ошибка в размерности матрицы B')
#
# c = addition_matrix(a, b, n, m)
# for row in c:
#     print(*row)


# import numpy as np
#
def matrix_multiplication(A:list,B:list) -> list:
    C = [[0]*len(B[0]) for _ in range(len(A))]
    if len(A[0]) != len(B):
        return C
    for i in range(len(A)):

        for j in range(len(B[0])):
            summa = 0
            for r in range(len(A[0])):
                summa += A[i][r]*B[r][j]
            C[i][j] = summa
    return C

def power_matrix(A:list,p:int) -> list:
    C = [[1]*len(A) for _ in range(len(A))]
    if not p:
        return C
    C = matrix_multiplication(A,A)
    for i in range(1,p-1):
        C = matrix_pultiplication(C,A)
    return C

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
p = int(input())
c = power_matrix(a, p)
for row in c:
    print(*row)
#
# n, m = map(int,input().split())
# A = [ list(map(int, input(f'{_}-я строка матрицы A:').split())) for _ in range(n)]
# #print(*A)
# B = [ list(map(int, input(f'{_}-я строка матрицы B:').split())) for _ in range(m)]
# #print(*B)
# C = matrix_multiplication(A, B)
# for i in range(24):
#     C = matrix_multiplication(C, C)
# for row in C:
#     print(*row)