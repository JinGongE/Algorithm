#print(ord('a')-96, ord('z')-96)
L = int(input())
string = input()

n=0
hashing = 0
for i in string:
    alpha = ord(i)-96
    hashing += alpha * (31 ** n)
    n+=1
    hashing %= 1234567891
print(hashing)