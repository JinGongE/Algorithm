arr = []

def FB(n):
    if n%5 == 0 and n%3 == 0:
        return "FizzBuzz"
    elif n%5 == 0:
        return "Buzz"
    elif n%3 == 0:
        return "Fizz"
    else:
        return n

for i in range(3):
    arr.append(input())

for i in range(3):
    try:
        print(FB(int(arr[i])+(3-i)))
        break
    except:
        pass