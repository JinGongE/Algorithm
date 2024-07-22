import math

N = int(input())
Sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirts = 0
for i in Sizes:
    shirts += math.ceil(i/T)
print(shirts)
print(N//P, N%P)