s = input().upper()
dic = {}
for i in s:
    if i not in dic.keys():
        dic[i] = s.count(i)

arr = list(dic.values())
arr.sort()
arr.reverse()
if len(s) == 0:
    print("?")
elif len(arr) > 1 and arr[0] == arr[1]:
    print("?")
else:
    for k, v in dic.items():
        if v == arr[0]:
            print(k)
            break