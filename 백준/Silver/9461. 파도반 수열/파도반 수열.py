T = int(input())
P = [1 for _ in range(101)]

for i in range(1, 101):
    if i<4:
        P[i] = 1
    else:
        P[i] = P[i-3] + P[i-2]

for i in range(T):
    n = int(input())
    print(P[n])