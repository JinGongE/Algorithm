n, m = map(int, input().split())
arr =[]
for a in range(1, n+1):
  arr.append(a)

for a in range(m):
  i, j = map(int, input().split())
  t_arr = arr[i-1:j]
  t_arr.reverse()
  c=0
  for b in range(i-1, j):
    arr[b] = t_arr[c]
    c+=1

for a in range(0, n):
  print(arr[a], end=' ')