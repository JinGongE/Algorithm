import sys
k, n = map(int, sys.stdin.readline().split())
arr = [] 

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        cables = 0
        for i in arr:
            cables += i//mid
    
        if cables >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end
  
    
for i in range(k):
    arr.append(int(sys.stdin.readline()))
arr.sort()
print(binary_search(1, max(arr)))
