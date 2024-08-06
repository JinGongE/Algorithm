import sys
input = sys.stdin.readline

n, m = map(int, input().split())
people = {}
result = []
for i in range(n):
    people[input().rstrip()] = 1

for i in range(m):
    name = input().rstrip()
    if name in people:
        result.append(name)

result.sort()
print(len(result))
for i in result:
    print(i)