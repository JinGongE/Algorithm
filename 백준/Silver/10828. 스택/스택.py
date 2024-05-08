import sys


stack = []
n = int(input())

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        print(stack.pop() if len(stack) > 0 else -1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == "top":
        print(stack[-1] if len(stack) > 0 else -1)