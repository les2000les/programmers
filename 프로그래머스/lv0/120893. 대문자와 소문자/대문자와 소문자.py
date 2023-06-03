def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper() == True:
            answer = answer + i.lower()
        else:
            answer = answer + i.upper() 
    return answer