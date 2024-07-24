n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
arr2 = list(map(int, input().split()))

counting = dict()
for i in arr:
    if i in counting.keys():
        counting[i] += 1
    else:
        counting[i] = 1


def binary_search(start, end, k):
    if start > end:
        return 0
    mid = (start + end)//2
    if arr[mid] == k:
        return counting[k]
    elif arr[mid] < k:
        return binary_search(mid+1, end, k)
    else:
        return binary_search(start, mid-1, k)


result = []
for i in arr2:
    result.append(binary_search(0, len(arr)-1, i))
print(*result)