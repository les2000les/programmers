def solution(n):
    answer = 0
    number = 0
    num = int(len(str(n)))
    for i in range(0, num): #3
        number = int(n/10**(num-1-i))
        n = n- number*10**(num-1-i)
        answer = answer + number
    
    return answer