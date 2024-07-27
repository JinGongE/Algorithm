n = int(input())

five = n//5
min = -1
for i in range(five, -1, -1):   #5로 나눈 최대 몫 ~ 0까지
    rest_sugar = n - 5*i
    if rest_sugar % 3 == 0:
        min = i + rest_sugar//3
        break
print(min)