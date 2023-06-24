def solution(my_string):
    answer = []
    string = list(my_string)
    for i in string:
        if i not in answer:
            answer.append(i)
        else:
            continue
    answer = ''.join(answer)
    return answer