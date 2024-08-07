n = int(input())
arr = list(map(int, input().split()))
arr.sort()

k = len(arr)
sum = 0
for i in arr:
    sum += i*k
    k-=1
print(sum)