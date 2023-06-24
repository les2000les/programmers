def solution(n):
    i = 1
    factorial = 1
    while(n>= factorial):
        i = i+1
        factorial = factorial*i
    answer = i-1
    return answer