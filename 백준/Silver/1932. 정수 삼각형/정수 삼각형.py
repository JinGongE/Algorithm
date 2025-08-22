import sys

input = sys.stdin.readline

n = int(input())
result = 0

tri = list([] for _ in range(n))

for i in range(n):
    tri[i]=list(map(int, input().split()))
    tri[i].extend(0 for _ in range(n-i-1))


for i in range(1, n):
    for j in range(i+1):
        if j==0: # 왼쪽 수
            tri[i][j] += tri[i-1][j]
        else:
            tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])

print(max(tri[n-1]))
