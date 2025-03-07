A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A*P
Y = B
if P > C:
    Y+=D*(P-C)

print(X if X<Y else Y)