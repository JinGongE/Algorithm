n, m = map(int, input().split())

arr = list(map(int, input().split()))
max = 0

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            total = arr[i] + arr [j] + arr[k]
            if total > max and total <= m:
                max = total

print(max)