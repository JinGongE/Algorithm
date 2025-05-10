"""
1. 아이디어
 - 처음 위치 -> 4방향 이동
 - BFS로 이동 & 방문 체크
 - 이동 할 때 마다 카운트 +1
 - 현재 위치가 (n, m) 이면 종료
 - 최소 칸 수 저장 & 매번 비교

2. 시간복잡도
    BFS
 - 모든 길이 열려있다는 가정 하에
   e: 4 * m * n
   v: m * n
   e + v = 5v = 5 * 100 * 100 = 50000

3. 자료구조
 - 그래프 전체 : int[][]
 - 방문 : bool[][]
 - Queue: BFS

"""
from collections import deque
import sys
input = sys.stdin.readline


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]          


n ,m = map(int, input().split())
map = [input() for _ in range(n)]
chk = [[False] * m for _ in range(n)]
dist = {}

for y in range(n):
    for x in range(m):
        dist[(x, y)] = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    chk[y][x] = True
    dist[(0, 0)] = 1

    while q:
        ex, ey = q.popleft()
        if ex == m-1 and ey == n-1:
            break
        for i in range(4):
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0<=nx<m and 0<=ny<n and chk[ny][nx] == False and map[ny][nx] == '1':
                    dist[(nx, ny)] = dist[(ex, ey)] + 1
                    q.append((nx, ny)) 
                    chk[ny][nx] = True

bfs(0, 0)
print(dist[(m-1, n-1)])
