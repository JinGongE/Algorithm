while True:
    arr = list(map(int, input().split()))

    if arr[0]==0 and arr[1]==0 and arr[2]==0: break
    else:
        c = max(arr)**2
        arr.remove(max(arr))
        a, b = arr[0]**2, arr[1]**2
        if a+b == c:
            print("right")
        else:
            print("wrong")