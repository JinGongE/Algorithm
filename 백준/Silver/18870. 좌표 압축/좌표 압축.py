N = input()
nums = list(map(int, input().split()))

sorted_nums=sorted(nums)

d = {}

idx = 0
for i in sorted_nums:
    if i not in d:
        d[i] = idx
        idx += 1
        

for i in nums:
    print(d[i], end=" ")