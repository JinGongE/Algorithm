from collections import deque


def dfs(g, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=' ')
        if node in g:
            for near in g[node]:
                dfs(g, near, visited)

def bfs(g, start):
    visited = set()
    q = deque([start])
    
    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            if node in g:
                q.extend(g[node])
        

n, m, v = map(int, input().split())

L = {}

for i in range(m):
    a, b = map(int, input().split())
    if a not in L:
        L[a] = []
    if b not in L:
        L[b] = []
    L[a].append(b)
    L[b].append(a)
    L[a].sort()
    L[b].sort()

dfs(L, v, set())
print()
bfs(L, v)