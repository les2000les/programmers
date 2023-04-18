def solution(n):
    answer = 0
    for i in range(1,n+1):
        if int(i%2) == 0:
            answer = answer + i
        else: answer = answer
    i = i+1
    return answer