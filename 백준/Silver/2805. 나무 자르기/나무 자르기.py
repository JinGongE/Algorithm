N, M = map(int, input().split())
trees = list(map(int, input().split()))

h = 0
start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2
    result = sum(i-mid if i-mid >= 0 else 0 for i in trees)
#    print(start, mid, end)
    if result >= M:
        start = mid+1
        if h < mid: h = mid
    else:
        end = mid-1
print(h)