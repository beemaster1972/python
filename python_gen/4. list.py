def verify_magic_matrix(n: int, matrix: list):
    res = 'NO'
    if not n:
        return res
    mtrx = {matrix[i][j] for i in range(n) for j in range(n)}
    if len(mtrx) != n ** 2 or 0 in mtrx:
        return res
    main_sum = sum(matrix[0])
    summa_main = sum([matrix[i][i] for i in range(n)])
    summa_secondary = sum([matrix[i][n - i - 1] for i in range(n)])
    transp_matrix = zip(*matrix)
    sums_column = [sum(row) for row in transp_matrix if sum(row) == main_sum]
    sums_row = [sum(row) for row in matrix[1:] if sum(row) == main_sum]
    if main_sum == summa_main and main_sum == summa_secondary and len(sums_row) == n - 1 and len(sums_column) == n:
        res = 'YES'
    return res


n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
print(verify_magic_matrix(n, matrix))


# st, lst, row = input().split(), [], []
# st.append(None)
# for i,c in enumerate(st):
#     row = [c] if not len(row) else row
#     if c == st[min(i+1, len(st)-1)]:
#         row.append(c)
#     else:
#         lst.append(row)
#         row = []
# print(lst)



# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# print(sum([i for row in list1 for i in row])/len([i for row in list1 for i in row]))