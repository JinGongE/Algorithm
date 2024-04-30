def getNum(num):
  total = 0
  while num//10 != 0:
    total += num%10
    num = num//10
  total += num
  return total

n = int(input())
ans = 0
for i in range(n):
  if (i+getNum(i) == n):
    ans = i
    break
print(ans)
