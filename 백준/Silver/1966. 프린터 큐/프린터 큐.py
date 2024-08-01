from collections import deque

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    arr = deque(map(int, input().split()))
    
    target = m

    seq = 1
    while len(arr) != 0:
        if arr[0] == max(arr):
            if target == 0:
                break
            a = arr.popleft()
            seq += 1
            target -= 1
        else:
            arr.append(arr.popleft())
            if target == 0:
                target = len(arr)-1
            else:
                target -= 1
    print(seq)