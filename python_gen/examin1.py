n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
m = []
for i in range(n):
    for j in range(n):
        if (j<i>=n-1-j or j>i>=n-1-j)and i!=j:
            m.append(lst[i][j])
#maximum = [lst[i][j] for j in range(n) for i in range(n) if j<i>=n-1-j or j>i>=n-1-j]
print(max(m))