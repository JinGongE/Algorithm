import sys

seq = []
n = int(sys.stdin.readline())

#입력
for i in range(n):
    seq.append(int(sys.stdin.readline()))

#수열 연산
oper = []
stack = []
k = 0
for i in seq:
    while k < i:
        k+=1
        oper.append('+')
        stack.append(k)
        #print(f'push: {k}')
    if stack[-1] == i:
        oper.append('-')
        a = stack.pop()
        #print(f"pop {a}")
    else:
        print("NO")
        break

if len(oper) == n*2:
    for i in oper:
        print(i)
    