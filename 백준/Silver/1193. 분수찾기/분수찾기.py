x = int(input())
i = 1
a = 1
while i < x:
    a+=1
    i+=a

for j in range(1, a+1):
    if i == x:
        if a%2 == 1:
            print(f"{j}/{a-(j-1)}")
        else:
            print(f"{a-(j-1)}/{j}")
        break
    else:
        i-=1