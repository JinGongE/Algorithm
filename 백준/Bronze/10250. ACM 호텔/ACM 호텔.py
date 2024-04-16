n = int(input())
for i in range(n):
    h, w, n = map(int, input().split())
    f, r =1, 1
    for j in range(n-1):
        f+=1
        if f > h:
            f=1
            r+=1
    print(str(f)+str(r).zfill(2))