n = int(input())
for i in range(n):
  s = input()
  cnt = 0
  pre = ''
  total =0
  for j in s:
    if j == "O":
      if pre =='O':
        cnt+=1
      else: cnt = 1
      total +=cnt
    pre = j
  print(total)
