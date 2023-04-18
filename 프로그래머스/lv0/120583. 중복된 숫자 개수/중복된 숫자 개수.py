def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer = answer + 1
        else: answer = answer + 0
        i = i + 1
    return answer