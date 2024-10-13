def solution(nums):
    types = len(set(nums))
    s = len(nums)//2
    answer = types if s>types else s
    return answer