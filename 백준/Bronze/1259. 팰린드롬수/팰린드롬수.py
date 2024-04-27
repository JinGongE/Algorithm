while True:
    s = input()
    if s =='0':
        break
    rs = s[::-1]
    if s==rs:
        print("yes")
    else:
        print("no")
       