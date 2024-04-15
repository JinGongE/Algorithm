n, m = map(int, input().split())
arr= []
for i in range(1, n+1):
    arr.append(i)

for a in range(m):
    i, j = map(int, input().split())
    t = arr[i-1]
    arr[i-1]=arr[j-1]
    arr[j-1]=t
    
for i in range(n):
    print(arr[i], end=' ')
