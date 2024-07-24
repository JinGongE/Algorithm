n = int(input())
arr = list(map(int, input().split()))

result = []
k = 1
for i in arr:
    result.insert(i, k)
    k+=1
print(str(result[::-1]).replace(',', '').replace('[', '').replace(']', ''))