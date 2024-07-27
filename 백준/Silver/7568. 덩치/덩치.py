n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

rank = []
for i in arr:
    s = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            s+=1
    rank.append(s)
print(*rank)
