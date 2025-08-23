N, M = map(int, input().split())
A = set(map(int, input().split()))
B = list(A)
B.sort()


def f(n, arr):
    if len(arr)==M:
        print(*arr)
        return
    for i in range(n, len(B)):
        arr_copy = arr.copy()
        arr_copy.append(B[i])
        f(i, arr_copy)
        
f(0, [])
