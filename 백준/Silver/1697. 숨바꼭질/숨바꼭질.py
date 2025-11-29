from collections import deque

n,m = map(int, input().split())

q = deque()
visited = [False] * 400000

q.append((n, 0))
visited[n] = True

TOL = abs(m-n)*2


while q:
    v, d = q.popleft()
    #print(q)
    if v == m:
        print(d)
        break
    else:
        if abs(m - (v+1)) <= TOL and not visited[v+1]:
            q.append((v+1, d+1))
            visited[v+1] = True
        if abs(m - (v - 1)) <= TOL and not visited[v-1]:
            q.append((v-1, d+1))
            visited[v - 1] = True
        if abs(m - (v * 2)) <= TOL and not visited[v*2]:
            q.append((v*2, d+1))
            visited[v*2] = True