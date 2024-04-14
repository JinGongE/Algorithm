n, m = map(int, input().split())
arr =[]
for i in range(n):
    arr.append(0)
for a in range(m):
    i, j, k = map(int, input().split())
    for b in range(i-1, j):
        arr[b] = k

for i in range(n):
    print(arr[i], end=' ')