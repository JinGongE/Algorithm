str = input().split('-')
result = 0
b=True
for c in str:
    if b:
        digit = map(int, c.split('+'))
        result += sum(digit)
        b = False
    else:
        digit = map(int, c.split('+'))
        result -= sum(digit)
print(result)