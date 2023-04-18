def solution(num_list):
    odd = 0
    even = 0
    for i in num_list:
        if i%2 ==0:
            odd = odd + 1  #홀수
        else:
            even = even + 1 #짝수
    answer = [odd, even]
    return answer