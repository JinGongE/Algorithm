n = int(input())

fives = 0

for i in range(1,n+1):
    if i%5==0:
        k = i
        while k%5==0:
            fives +=1
            k/=5

print(fives)