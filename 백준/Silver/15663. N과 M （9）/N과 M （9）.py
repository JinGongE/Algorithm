N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

B=set()

def f(arr, Arr):
    if len(arr)==M:
        B.add(tuple(arr))
        return
    for i in Arr:
        arr_copy = arr.copy()
        Arr_copy = Arr.copy()
        arr_copy.append(i)
        Arr_copy.remove(i)
        f(arr_copy, Arr_copy)


f([], A.copy())

for i in sorted(B):
    print(*i)