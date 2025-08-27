import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    stickers = []
    dp = [([0] * n) for _ in range(2)]

    stickers.append(list(map(int, input().split())))
    stickers.append(list(map(int, input().split())))

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    if n > 1:
        dp[0][1] = max(stickers[0][1], dp[1][0]+stickers[0][1])
        dp[1][1] = max(stickers[1][1], dp[0][0]+stickers[1][1])
    
    if n > 2:
        for j in range(2, n):
            dp[0][j] = max(stickers[0][j]+dp[0][j-2], stickers[0][j]+dp[1][j-2], stickers[0][j]+dp[1][j-1])
            dp[1][j] = max(stickers[1][j]+dp[0][j-2], stickers[1][j]+dp[1][j-2], stickers[1][j]+dp[0][j-1])

    print(max(dp[0][n-1], dp[1][n-1]))
    #print(dp)