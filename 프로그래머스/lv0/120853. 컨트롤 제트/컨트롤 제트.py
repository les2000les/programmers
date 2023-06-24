def solution(s):
    answer = 0
    num = s.split(' ')
    for i in num:
        if i !='Z':
            answer = answer+int(i)
            last = int(i)
        else:
            answer = answer - last
    return answer