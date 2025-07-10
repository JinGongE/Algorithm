import sys

input = sys.stdin.readline

N = 5
nums=[]

for i in range(N):
    nums.append(int(input()))
    
    
print(int(sum(nums)/N), sorted(nums)[N//2], sep='\n')