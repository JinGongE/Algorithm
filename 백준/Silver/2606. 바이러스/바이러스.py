import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
l = int(input())

com = dict()

for i in range(1, n+1):
    com[i] = set()

for i in range(1, l+1):
    a, b = map(int, input().rstrip().split())
    com[a].add(b)
    com[b].add(a)

visited = set()
queue = deque()
queue.append(1)
while len(queue) != 0:
    v = queue.popleft()
    visited.add(v)
    for i in com[v]:
        if i not in visited:
            visited.add(i)
            queue.append(i)
    #print(f"{v} -> ", end='')
print(len(visited)-1)