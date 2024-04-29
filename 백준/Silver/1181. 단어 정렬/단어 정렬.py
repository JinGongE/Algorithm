n = int(input())
arr = []
for i in range(n):
  arr.append(input())

for i in arr:
  while arr.count(i)>1:
    arr.remove(i)

arr.sort(key=lambda x: (len(x), x))
for i in arr:
  print(i)
