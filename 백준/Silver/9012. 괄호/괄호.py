import sys
n = int(input())

for i in range(n):
    data = sys.stdin.readline().rstrip()
    stack = []
    a = True
    for j in data:
        if j == '(':
            stack.append(j)
        else:
            try:
                stack.pop()
            except:
                print("NO")
                a = False
                break
    if a == True:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")

    