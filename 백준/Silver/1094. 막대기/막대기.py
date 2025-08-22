
n = int(input())
s = 64
l = 0
sticks = 0

for i in range(6, -1, -1):
    if l+2**i <= n:
        sticks+=1
        l+=2**i
    if l == n:
        print(sticks)
        break