import sys

n = int(input())

max = [0, 9999, 9999]
num = 0
for i in range(n):
    p = list(map(int, sys.stdin.readline().split()))
    if p[0] > max[0]:
        max = p
        num = i+1
    elif p[0] == max[0] and p[1] < max[1]:
        max = p
        num = i+1
    elif p[0] == max[0] and p[1] == max[1] and p[2] < max[2]:
        max = p
        num = i+1

print(num)
