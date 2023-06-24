def solution(n):
    answer = 0
    
    numcount = 0
    for i in range(1, n+1): # n 이하의 수 중에서
        count = 0
        for j in range(1,i+1): # 약수 찾기(2~n)
            if i % j == 0: 
                count = count+1
            else:
                continue
        if count >= 3:
            numcount = numcount+1
        else:
            continue
    return numcount