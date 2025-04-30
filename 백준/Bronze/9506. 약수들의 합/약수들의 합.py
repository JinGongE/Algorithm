while True:
    n = int(input())
    if n == -1:
        break
    
    formula = "1"
    sum = 1
    for i in range(2, n):
        if n%i == 0:
            formula += f" + {i}"
            sum += i
    if sum == n:
        print(f"{n} =", formula)
    else:
        print(f"{n} is NOT perfect.")