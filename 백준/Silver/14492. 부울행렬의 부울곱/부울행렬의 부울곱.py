n = int(input())
total = 0
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = []
for i in range(n):
    b.append(list(map(int, input().split())))

c = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i][k] == 1 and b[k][j] == 1:
                c[i][j] = 1
                total += 1
                break;

# for i in range(n):
#     print(a[i])
# print()
# for i in range(n):
#     print(b[i])
# print()
# for i in range(n):
#     print(c[i])

print(total)