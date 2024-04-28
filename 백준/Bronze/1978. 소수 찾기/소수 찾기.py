n = int(input())
arr = list(map(int, input().split()))
cnt = 0

def getDivisors(num):
    return [i for i in range(1, num+1) if num%i==0]

for i in arr:
    if len(getDivisors(i)) == 2:
        cnt += 1
print(cnt)