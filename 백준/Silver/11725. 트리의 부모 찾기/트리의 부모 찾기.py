import sys
from collections import deque
sys.setrecursionlimit(10**5+10)

input = sys.stdin.readline

N = int(input())

q = deque()

parent = list(0 for _ in range(N+1))

l_list = list([] for _ in range(N+1))
visited = [0] * (N+1)

for i in range(N-1):
    k, v = map(int, input().split())
    l_list[k].append(v)
    l_list[v].append(k)


q.append(1)

while(len(q)):
    v = q.popleft()
    visited[v] = 1
    

    for i in l_list[v]:
        if visited[i] == 0:
            q.append(i)
            parent[i] = v

for i in range(2, N+1):
    print(parent[i])
    