def solution(my_string, n):
    answer = []
    for i in my_string:
        for j in range(1, n+1):
            answer.append(i)
    return ''.join(answer)