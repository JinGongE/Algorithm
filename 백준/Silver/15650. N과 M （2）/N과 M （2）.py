n, m = map(int, input().split())
arr = [0 for _ in range(m)]
def getNum(a, idx):
    if idx >= m:
        return
    elif a >n:
        return
    else:
        arr[idx] = a
        if idx == m-1: print(*arr)
        getNum(a+1, idx+1)
        getNum(a+1, idx)
getNum(1, 0)
