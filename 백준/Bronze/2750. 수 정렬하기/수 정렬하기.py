import sys

input = sys.stdin.readline

N = int(input())
nums=[]

for i in range(N):
    nums.append(int(input()))
    

sorted_nums=sorted(nums)

print(*sorted_nums, sep="\n")