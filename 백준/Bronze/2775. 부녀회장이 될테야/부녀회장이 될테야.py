t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    fl = [i for i in range(1, n+1)]

    for x in range(k):   #층
        nf = []
        for y in range(n):  #호
            nf.append(sum(fl[:y+1]))
        fl = nf.copy()
    print(fl[-1])
