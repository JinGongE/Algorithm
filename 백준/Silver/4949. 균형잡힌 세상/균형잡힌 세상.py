import sys

arr = []
while True:
    arr.append(sys.stdin.readline().rstrip())
    if arr[-1] == '.':
        arr.pop()
        break

for i in arr:
    small, big = 0, 0
    stack = []
    check = True
    for j in i:
        if j == '(':
            stack.append(1)
        elif j == '[':
            stack.append(2)
        elif j == ')':
            if len(stack) == 0 or stack[-1] != 1:
                print("no")
                check = False
                break
            else:
                stack.pop()
        elif j == ']':
            if len(stack) == 0 or stack[-1] != 2:
                print("no")
                check = False
                break
            else:
                stack.pop()
    
    if check == True:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")