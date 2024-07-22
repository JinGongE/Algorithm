import sys

def roundUp(n):
    if n - int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

if n == 0: print(0)
else:
    exc = roundUp(n/100*15)
    total = 0
    for i in range(exc, n-exc):
        total += arr[i]
    print(roundUp(total / (n-exc*2)))