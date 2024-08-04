import sys

def round(k):
    if abs(k)-abs(int(k)) >= 0.5:
        if k < 0:
            return int(k)-1
        else:
            return int(k)+1
    else:
        return int(k)

n = int(input())
dict_data = dict()
list_data = []

for i in range(n):
    k = int(sys.stdin.readline())
    list_data.append(k)
    if k not in dict_data:
        dict_data[k] = 1
    else:
        dict_data[k] += 1

list_data.sort()
dict_data = dict(sorted(dict_data.items(), key=lambda items: (-items[1], items[0])))
keys = list(dict_data.keys())
values = list(dict_data.values())

if len(keys) == 1:
    many = keys[0]
elif values[0] == values[1]:
    many = keys[1]
else:
    many = keys[0]

average = round(sum(list_data)/n)
middle = list_data[n//2]
ranges = list_data[-1] - list_data[0]
print(average, middle, many, ranges, sep='\n')