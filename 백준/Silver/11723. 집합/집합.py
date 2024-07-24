import sys

m = int(input())
s = set()

for i in range(m):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "all":
        s = set(range(1, 21))
    elif cmd == "empty":
        s.clear()
    else:
        cmd, value = cmd.split()
        if cmd == "add":
            s.add(int(value))
        elif cmd == "remove":
            if int(value) in s: s.remove(int(value))
        elif cmd == "check":
            if int(value) in s: print(1)
            else: print(0)
        elif cmd == "toggle":
            if int(value) in s: s.remove(int(value))
            else: s.add(int(value))