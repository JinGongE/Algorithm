a, b = map(int, input().split())
o_a, o_b = a, b
while b!=0:
  r = a%b
  a, b = b, r

print(a)
print(int(o_a*o_b/a))