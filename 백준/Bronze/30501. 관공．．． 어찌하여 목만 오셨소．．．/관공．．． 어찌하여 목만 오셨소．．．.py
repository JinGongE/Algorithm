import sys
n = int(sys.stdin.readline())

for i in range(n):
    name = sys.stdin.readline()
    if 'S' in name:
        print(name)