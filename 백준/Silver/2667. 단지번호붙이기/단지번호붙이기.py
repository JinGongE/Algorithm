grid = []
visited = [[False] * 25 for _ in range(25)]
aparts = []

def dfs(r, c, n):
    if r >= n or r < 0 or c >= n or c < 0:
        return 0
    elif visited[r][c] == True:
        return 0
    elif grid[r][c] == '0':
        return 0
    else:
        sum = 1
        visited[r][c] = True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            sum += dfs(r + dr, c + dc, n)
        return sum

n = int(input())
for i in range(n):
    grid.append(input())

for i in range(n):
    for j in range(n):
        k = dfs(i, j, n)
        if k != 0:
            aparts.append(k)

aparts.sort()

print(len(aparts))
for i in aparts:
    print(i)