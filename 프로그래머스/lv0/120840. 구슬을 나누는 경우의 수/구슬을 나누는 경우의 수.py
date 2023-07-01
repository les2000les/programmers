def solution(balls, share):
    answer = 0
    num_d = 1
    num_u = 1
    for i in range(1, share+1): #분모: share ~1 까지 곱
        num_d = num_d*i
        
    for j in range(balls-share+1, balls+1): #ball부터 share까지 곱
        num_u = num_u*j
         
    answer = num_u/num_d
    return answer