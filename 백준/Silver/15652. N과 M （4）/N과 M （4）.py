N, M = map(int, input().split())


def f(n, arr):
    if len(arr)==M:
        print(*arr)
        return
    for i in range(n, N+1):
        arr_copy = arr.copy()
        arr_copy.append(i)
        f(i, arr_copy)


f(1, [])