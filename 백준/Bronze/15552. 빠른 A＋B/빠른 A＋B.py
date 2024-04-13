import sys
n = sys.stdin.readline().rstrip()

for i in range(int(n)):
    a, b = sys.stdin.readline().split()
    print(int(a)+int(b))