import sys
n = sys.stdin.readline().rstrip()

for i in range(int(n)):
    print(" "*(int(n)-(i+1)) + "*"*(i+1))