
a, b, c = map(int, input().split())

for i in range(1, 30):
    if (b+1==c and c%2==0) or (c+1==b and b%2==0):
        print(i)
        break
    else:
        b = b//2 + b%2
        c = c//2 + c%2
