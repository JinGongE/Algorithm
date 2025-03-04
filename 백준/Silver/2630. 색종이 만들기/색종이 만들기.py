
def f(x, y, n):
    if n==1:
        color[arr[y][x]] += 1
        return
    ar = list()
    for i in range(y, y+n):
        ar.extend(arr[i][x:x+n])
    if all(k == ar[0] for k in ar):
        color[ar[0]] += 1
    else:
        n = n//2
        f(x, y, n)
        f(x+n, y, n)
        f(x, y+n, n)
        f(x+n, y+n, n)

n = int(input())
arr = list()
color = [0, 0]
for i in range(n):
    arr.append(list(map(int, input().split())))
f(0, 0, n)
print(color[0])
print(color[1])