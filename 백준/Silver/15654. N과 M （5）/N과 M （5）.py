
def solution(numbers: list, result: list):
    if len(result) == m:
        print(*result)
    for i in numbers:
        temp_lst = [*numbers]
        temp_lst.remove(i)
        temp_lst2 = [*result]
        temp_lst2.append(i)
        #print(numbers, temp_lst, temp_lst2, result)
        solution(temp_lst, temp_lst2)
        


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

solution(lst, [])
