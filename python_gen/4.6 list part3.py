import numpy as np
import itertools
n, m = map(int, input().split())
matrix = np.zeros((n, m),int) # создаем нулевую матрицу n на m
Dim = itertools.cycle((m,n)) # бесконечный цикл для определения текущей размерности строки матрицы
num, i, fl = 1, 0, False
while num <= n*m:
    for _ in range(4):
        N = next(Dim)
        for j in range(i, N-i):
            if matrix[i][j]:
                continue
            matrix[i][j] = num
            num += 1
            if num > n*m:
                fl = True
                break
        matrix = np.rot90(matrix)
    i += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3),end='')
    print()
# n, m = map(int, input().split())
# nm = 0
# matrix = [[j+1+m*i for j in range(m)] for i in range(n)]
# for q in range(n+m-2):
#     for i in range(n):
#         for j in range(m):
#             if i+j == q:
#                 nm += 1
#                 matrix[i][j] = nm
#
# for row in matrix:
#     print(*row)



# n, m = map(int, input().split())
# matrix = [[j+1+m*i for j in range(m)] for i in range(n)]
# for i in range(1,n,2):
#     matrix[i].reverse()
# for row in matrix:
#     print(*row)


# n,m = map(int, input().split())
# matrix = [[j+1 for j in range(m)]]
# for i in range(1,n):
#     matrix.append(matrix[i-1][1:]+matrix[i-1][:1])
#     # for j in range(m):
#     #     matrix.append(matrix[i-1][j]+1 if j != m-1 else )
# for row in matrix:
#     print(*row)

# n,m = map(int, input().split())
# matrix = [['.*'[(j+i) % 2] for j in range(m)] for i in range(n)]
# for row in matrix:
#     print(*row)



# if n > 1:
#     matrix = [[matrix[j:j+m]] for j in range(0,n*m,m)]
