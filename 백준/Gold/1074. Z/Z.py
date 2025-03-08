N, r, c = map(int, input().split())
result = 0
n = 2**N
for i in range(1, N+1):
    d = n//(2**i)
    a = 0
    if r >= d:
        a+=2
        r-=d
    if c >= d:
        a+=1
        c-=d
    result += d*d*a
print(result)