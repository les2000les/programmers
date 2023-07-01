def solution(my_string):
    my_string = my_string.split(' ')
    answer = 0
    operator = 0
    for index, i in enumerate(my_string):
        if index%2 != 0: #연산자인 경우
            if i == '+':
                operator = 1
            else:
                operator = 2
        else:
            if operator == 0: #맨 처음 값
                answer = int(i)
            elif operator == 1: #+일경우
                answer = answer + int(i)
            else: #-일 경우
                answer = answer - int(i)  
    return answer  