import sys
input = sys.stdin.readline

N = int(input())
l = []
for _  in range(N):
    l.append(list(map(int, input().split())))

l.sort(key=lambda x: (x[1], x[0]))


t = 0
count = 0
for i in l:
    if i[0] >= t:
        count+=1
        t=i[1]
print(count)

