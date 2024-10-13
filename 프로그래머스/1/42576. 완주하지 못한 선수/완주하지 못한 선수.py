def solution(participant, completion):
    a = {}
    for i in participant:
        if i not in a: a[i] =0
        a[i] += 1
    for i in completion:
        a[i] -= 1
    answer = ''
    for x, n in a.items():
        if n==1:
            answer = x 
    return answer