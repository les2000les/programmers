def solution(box, n):
    answer = 1
    for i in range(0, len(box)):
        answer = answer * int((box[i])/n)
    return answer