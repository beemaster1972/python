lst_in = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]
          ]
a = [x
     for row in lst_in[-1::-1]
     for x in row[-1::-1]
     ]
print(*a)
# lst_in = [[2, 3, 4, 5, 6],
#           [3, 2, 7, 8, 9],
#           [4, 7, 2, 0, 4],
#           [5, 8, 0, 2, 1],
#           [6, 9, 4, 1, 2]]
# fl = True
# for i in range(len(lst_in)):
#     for j in range(len(lst_in[0])):
#         if i == j:
#             continue
#         if lst_in[i][j] != lst_in[j][i]:
#             fl = False
#             print('НЕТ')
#             break
#     if not fl:
#         break
# else:
#     print('ДА')

# lst_in =[[1, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 1, 0, 1, 0],
# [0, 0, 0, 0, 0]]
#
# fl = True
#
# for i in range(len(lst_in)-1):
#     for j in range(len(lst_in[0])-1):
#         if lst_in[i][j] + lst_in[i+1][j+1] + lst_in[i+1][j] + lst_in[i][j+1] > 1:
#             fl = False
#             print('НЕТ')
#             break
#     if not fl:
#         break
# else:
#     print('ДА')
