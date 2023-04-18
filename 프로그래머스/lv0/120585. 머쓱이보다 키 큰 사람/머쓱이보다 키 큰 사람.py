def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer = answer + 1
        else : answer = answer + 0
        i = i+1
    return answer