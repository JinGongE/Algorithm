arr = []
for i in range(1, 31):
  arr.append(i)

for i in range(28):
  arr.remove(int(input()))

arr.sort()
print(arr[0])
print(arr[1])