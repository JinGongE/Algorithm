import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dic = {}

for i in range(1, n+1):
    s = sys.stdin.readline().rstrip()
    dic[i] = s

rev_dic = {v:k for k, v in dic.items()}
for i in range(m):
    s = sys.stdin.readline().rstrip()
    if s.isdigit():
        ans = dic[int(s)]
    else:    
        ans = rev_dic[s]
    print(ans)