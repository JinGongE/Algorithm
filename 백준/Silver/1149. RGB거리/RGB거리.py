import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
dp = [[0, 0, 0] for _ in range(n)]
cost = []

for i in range(n):
    cost.append(list(map(int, input().split())))

dp[0][0] = cost[0][0];
dp[0][1] = cost[0][1];
dp[0][2] = cost[0][2];

for idx in range(1, n):
    for color in range(3):
        if dp[idx][color] == 0:
            colors = [0, 1, 2]
            colors.remove(color)
            # 현재 색을 제외한 두 색깔 가격 중 가장 낮은 가격으로.
            costs = []
            for c in colors:
                costs.append(dp[idx-1][c] + cost[idx][color])
            dp[idx][color] = min(costs)

print(min(dp[n-1]))