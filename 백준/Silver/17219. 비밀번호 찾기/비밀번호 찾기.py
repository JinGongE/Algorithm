import sys
n, m = map(int, sys.stdin.readline().split())

dic = dict()

for i in range(n):
    domain, pw = sys.stdin.readline().rstrip().split()
    dic[domain] = pw

for i in range(m):
    domain = sys.stdin.readline().rstrip()
    print(dic[domain])