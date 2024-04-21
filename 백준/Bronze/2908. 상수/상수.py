a, b = input().split()
r_a= int(f"{a[2]}{a[1]}{a[0]}")
r_b= int(f"{b[2]}{b[1]}{b[0]}")
if r_a > r_b:
    print(r_a)
else:
    print(r_b)