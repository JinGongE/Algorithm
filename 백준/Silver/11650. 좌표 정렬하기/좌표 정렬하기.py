import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

arr.sort()
for i in arr:
    print(i[0], i[1])