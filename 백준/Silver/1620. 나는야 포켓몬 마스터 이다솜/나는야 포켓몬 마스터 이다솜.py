import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dic = {}

for i in range(1, n+1):
    s = sys.stdin.readline().rstrip()
    dic[i] = s

rev_dic = {v:k for k, v in dic.items()}
for i in range(m):
    s = sys.stdin.readline().rstrip()
    try:
        ans = dic[int(s)]
    except:
        
        ans = rev_dic[s]
    print(ans)