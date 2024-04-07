n, m = map(int, input().split())

arr = list(range(1, n+1))

for a in range(m):
    i, j = map(int, input().split())

    temp_arr = arr[i-1:j]
    temp_arr.reverse()
    count = 0
    for b in range(i-1, j):
        arr[b] = temp_arr[count]
        count+=1

for i in range(n):
    print(arr[i], end=' ')