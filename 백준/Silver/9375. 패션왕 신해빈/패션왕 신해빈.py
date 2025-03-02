from functools import reduce

n = int(input())

for i in range(n):
    nn = int(input())
    clothes = {}
    for j in range(nn):
        v, k = input().split(" ")
        if k in clothes.keys():
            clothes[k] += 1
        else:
            clothes[k] = 2
    print(reduce(lambda x, y: x*y, clothes.values())-1 if len(clothes) > 0 else 0)