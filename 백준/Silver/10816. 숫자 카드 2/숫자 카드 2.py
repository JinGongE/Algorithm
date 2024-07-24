n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
arr2 = list(map(int, input().split()))

counting = dict()
for i in arr:
    if i in counting.keys():
        counting[i] += 1
    else:
        counting[i] = 1

result = []

for i in arr2:
    if i in counting: result.append(counting[i])
    else: result.append(0)
print(*result)