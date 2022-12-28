# R = 5
w = 0
P = [[1]]
R = int(input("Введите высоту треугольника Паскаля"))
if R <= 5:
    w = 3
elif R <=7:
    w = 4
elif R >= 8:
    w = 4


def print_triangle(matrix):
    global w
    for i in range(len(matrix)):
        print(f'11^{i:2} = ', end = '')
        tab = (int((R * w) / 2) - i)-2
        if i != R:
            tab += 1
        print((' ' * tab), end='')
        for j in range(i + 1):
            if R <= 5:
                s = f'{matrix[i][j]:^2}'
            elif R <= 7:
                s = f'{matrix[i][j]:^3}'
            elif R >= 8:
                s = f'{matrix[i][j]:^4}'
            print(s, end='')
        print('')


for i in range(1, R):
    row = []
    for j in range(i + 1):
        row.append(1 if j == 0 or j == i else P[i - 1][j - 1] + P[i - 1][j])
    P.append(row)
# print(P)
print_triangle(P)
