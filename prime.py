import math
import time
n, k = int(input()), 1
start_time = time.time()
fl = True
print(2, end=' ')
for i in range(3, n, 2):
    fl = True
    for j in range(3, math.floor(pow(i, 1/2))+1, 2):
        if i % j == 0:
            fl = False
            break
    if fl:
        k += 1
        print(i, end=" ")
        if k % 10 == 0:
            print()
end_time = time.time()
delta = end_time - start_time
print(f"Затрачено на нахождение {k} простых чисел {delta} сек.")